/* ALPINE_POLICY_START — shared by the standalone game and the Jev adapter. */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.AlpinePolicy = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const VERSION='feedback-policy-4.1.0', CONTRACT='alpine-jev-1';
  const ACTIONS=['easier','same','harder','support','variety','pause'];
  const GOALS=['look_ahead','gentle_turns','return_centre','safe_coins','route_choice'];
  const REASONS=['speed','instructions','visibility','coins','turns','tired','more_challenge','other'];
  // Engineering defaults for this self-test; these are NOT validated learning thresholds.
  const GATES={actionConfidence:.55,harderProbability:.80,goalConfidence:.45};
  const clamp=(v,a,b)=>Math.min(b,Math.max(a,v));
  const number=(v,f=null)=>typeof v==='number'&&Number.isFinite(v)?v:f;
  const bounded=(v,a,b,f=null)=>number(v)===null?f:clamp(v,a,b);
  const round=v=>Math.round(v*1000)/1000;
  const member=(v,values,f=null)=>values.includes(v)?v:f;
  const COMPLETIONS=['time_complete','ended_at_bump_limit','partial','interrupted','unknown'];
  const ENDINGS=['player_stop','player_finished','time','time_cap','gameover','bump_limit','interrupted','unknown'];
  const INPUTS=['keys','touch','tilt','pad','keys+','touch+','tilt+','pad+','none'];

  function metrics(r) {
    if(!r)return {faced:0,hits:0,clearRate:null,coinRate:null,coins:0,missed:0,edgePct:null,seconds:0};
    const faced=Math.floor(bounded(r.Obstacles_Faced,0,10000,0));
    const hits=Math.floor(bounded(r.Obstacles_Hit,0,faced,0));
    const coins=Math.floor(bounded(r.Coins,0,10000,0)),missed=Math.floor(bounded(r.Coins_Missed,0,10000,0));
    return {faced,hits,clearRate:faced?(faced-hits)/faced:null,coinRate:coins+missed?coins/(coins+missed):null,
      coins,missed,edgePct:bounded(r.Edge_Time_pct,0,100),seconds:bounded(r.Duration_s,0,3600,bounded(r.Duration_Min,0,60,0)*60)};
  }
  function cleanReport(f={},allowText=false) {
    const skipped=f.skipped===true;
    return {difficulty:skipped?null:member(f.difficulty,['easy','right','hard']),
      feeling:skipped?null:member(f.feeling,['enjoying','okay','frustrated','tired','bored']),
      reason:skipped?null:member(f.reason,REASONS),skipped,
      text:!skipped&&allowText&&typeof f.text==='string'?f.text.slice(0,400):''};
  }
  function observation(r={},report={}) {
    const m=metrics(r),start=bounded(r.Start_Diff,.4,2.2),end=bounded(r.AI_DiffMult,.4,2.2);
    return {metrics:m,level:bounded(r.Mean_Diff,.4,2.2,end),startLevel:start,endLevel:end,
      support:member(r.Support,['none','route_guide'],'unknown'),
      goal:member(r.Practice_Goal,GOALS),input:member(r.Input_Mode,INPUTS,'none'),
      completion:member(r.Completion_Status,COMPLETIONS,r.Counted==='FALSE'?'partial':'unknown'),
      endReason:member(r.End_Reason,ENDINGS,'unknown'),report:cleanReport(report)};
  }
  function sanitizeObservation(o={}) {
    const m=o.metrics||{};
    const result=observation({Obstacles_Faced:m.faced,Obstacles_Hit:m.hits,Coins:m.coins,Coins_Missed:m.missed,
      Edge_Time_pct:m.edgePct,Duration_s:m.seconds,Mean_Diff:o.level,Start_Diff:o.startLevel,
      AI_DiffMult:o.endLevel,Support:o.support,Practice_Goal:o.goal,Input_Mode:o.input,
      Completion_Status:o.completion,End_Reason:o.endReason},o.report||{});
    // Never accept a client/model-supplied clearance rate: derive it from event counts.
    return result;
  }
  function summarize(observations,reference) {
    const recent=observations.slice(-12);
    const stable=o=>o.startLevel!==null&&o.endLevel!==null&&Math.abs(o.startLevel-o.endLevel)<=.01;
    const comparable=recent.filter(o=>o.metrics.faced>0&&o.level!==null&&reference.level!==null&&
      Math.abs(o.level-reference.level)<=.01&&o.support!=='unknown'&&o.support===reference.support&&
      o.input!=='none'&&o.input===reference.input&&stable(o)&&stable(reference));
    const faced=comparable.reduce((n,o)=>n+o.metrics.faced,0),hits=comparable.reduce((n,o)=>n+o.metrics.hits,0);
    return {recentRuns:recent.length,comparableRuns:comparable.length,comparableFaced:faced,
      comparableClearRate:faced?(faced-hits)/faced:null,
      partialRuns:recent.filter(o=>o.completion==='partial').length,
      interruptedRuns:recent.filter(o=>o.completion==='interrupted').length,
      bumpLimitedRuns:recent.filter(o=>o.completion==='ended_at_bump_limit').length,
      status:'Descriptive observations grouped by matching pace, support and input. Not a validated mastery or difficulty-adjusted learning score.'};
  }
  function learnerEstimate(runs,reference,feedbackHistory=[]) {
    const records=(runs||[]).filter(r=>r.Run_Type==='play').slice(-12);
    const observations=records.map(r=>observation(r,feedbackHistory.find(f=>f.runId===r.Run_ID)||{}));
    return {...summarize(observations,observation(reference||records[records.length-1]||{})),observations};
  }
  function stateFromGame({last,runs,feedback,level,feedbackHistory=[],language='en'},allowText=false) {
    const report=cleanReport(feedback||{},allowText);
    const current=observation(last||{},report);
    const history=learnerEstimate(runs,last,feedbackHistory).observations;
    return {schema:CONTRACT,language:member(language,['en','zh','zhs'],'en'),
      currentLevel:bounded(level,.4,2.2,bounded(last&&last.AI_DiffMult,.4,2.2,.85)),current,history,report};
  }
  function sanitizeState(s={},allowText=false) {
    if(s.schema!==CONTRACT)throw new Error('Unsupported request schema');
    if(!s.current||!s.current.metrics)throw new Error('Missing current performance');
    return {schema:CONTRACT,language:member(s.language,['en','zh','zhs'],'en'),
      currentLevel:bounded(s.currentLevel,.4,2.2,.85),current:sanitizeObservation(s.current),
      history:(Array.isArray(s.history)?s.history:[]).slice(-12).map(sanitizeObservation),report:cleanReport(s.report||{},allowText)};
  }
  function hintFromText(text) {
    let s=String(text||'').normalize('NFKC').toLowerCase().slice(0,400);
    s=s.replace(/\b(?:not|never)\s+(?:(?:very|at all)\s+)?(?:tired|hard|difficult|fast|confused)\b/g,' ')
      .replace(/不(?:太|是很|覺得|觉得)?(?:累|疲倦|難|难|快)/g,' ');
    const patterns=[['tired',/\btired\b|\bfatigu|\bexhaust|疲|累/],
      ['instructions',/\bconfus|\binstruction|\bunderstand|不懂|不明|說明|说明/],
      ['visibility',/\bsee\b|\bsmall\b|\bvisib|看不|太小|顏色|颜色/],
      ['speed',/\bfast\b|\bquick\b|\bspeed\b|\bslow\b|太快|速度|慢一/],
      ['coins',/\bcoin|金幣|金币/],['turns',/\bturn|\bsteer|轉|转|操控/],
      ['more_challenge',/\bbored\b|too easy|more challeng|harder|太容易|無聊|无聊|更難|更难/]];
    const tags=patterns.filter(([,re])=>re.test(s)).map(([tag])=>tag);
    return {tags,ambiguous:tags.length!==1,method:'keyword-suggestion-only',requiresConfirmation:true};
  }
  function chooseGoal(current,fb,action) {
    if(fb.reason==='coins')return 'safe_coins';
    if(fb.reason==='turns')return 'gentle_turns';
    if(fb.reason==='instructions'||fb.reason==='visibility')return 'route_choice';
    if(action==='variety')return GOALS[(Math.max(0,GOALS.indexOf(current.goal))+1)%GOALS.length];
    if(current.metrics.edgePct!==null&&current.metrics.edgePct>=50)return 'return_centre';
    return current.goal||'look_ahead';
  }
  function materialize(action,base,goal,reasonCode,source='local-rules') {
    base=clamp(number(base,.85),.40,2.20);
    if(!ACTIONS.includes(action))action='same';
    if(!GOALS.includes(goal))goal='look_ahead';
    const level=round(clamp(base+(action==='easier'?-.12:action==='harder'?.10:0),.40,2.20));
    return {policyVersion:VERSION,action,baseLevel:round(base),level,duration:action==='pause'?20:30,
      support:['support','variety'].includes(action)?'route_guide':'none',goal,reasonCode,source,
      maxChange:.15,challengeChanged:Math.abs(level-base)>.0001};
  }
  function upwardAllowed(s,summary) {
    const m=s.current.metrics,f=s.report;
    return (f.difficulty==='easy'||f.reason==='more_challenge'||f.feeling==='bored')&&
      f.difficulty!=='hard'&&f.feeling!=='frustrated'&&f.feeling!=='tired'&&
      !['instructions','visibility','tired'].includes(f.reason)&&m.faced>=6&&m.clearRate>=.80&&
      m.edgePct!==null&&m.edgePct<50&&
      (summary.comparableClearRate===null||summary.comparableFaced<12||summary.comparableClearRate>=.75);
  }
  function proposeState(s) {
    const f=s.report,m=s.current.metrics,summary=summarize(s.history,s.current);
    let action='same',why='consolidate';
    if(f.feeling==='tired'||f.reason==='tired'){action='pause';why='reported_tired';}
    else if(f.reason==='instructions'||f.reason==='visibility'){action='support';why='reported_clarity';}
    else if(f.difficulty==='hard'&&f.feeling==='enjoying'){action='support';why='welcome_challenge';}
    else if(f.difficulty==='hard'||f.feeling==='frustrated'){action='easier';why='reported_demand';}
    else if(f.feeling==='bored'||f.reason==='more_challenge'||f.difficulty==='easy'){
      if(upwardAllowed(s,summary)){action='harder';why='ready_for_challenge';}
      else{action='variety';why='mixed_evidence';}
    }else if(f.reason==='speed'){action='easier';why='reported_demand';}
    else if(m.faced>=3&&m.clearRate<.55){action='easier';why='recorded_errors';}
    else if(m.faced<3){why='limited_evidence';}
    const p=materialize(action,s.currentLevel,chooseGoal(s.current,f,action),why);
    p.evidence={performance:m,learnerEstimate:{...summary,observations:s.history},feedbackUsed:!f.skipped,
      difficulty:f.difficulty,feeling:f.feeling,reason:f.reason,upwardAllowed:upwardAllowed(s,summary)};
    return p;
  }
  function propose(args){return proposeState(stateFromGame(args));}
  function validateRemote(candidate,local) {
    if(!candidate||candidate.provider!=='typesafe'||candidate.contract!==CONTRACT)throw new Error('Unexpected decision provider');
    if(candidate.status==='uncertain'||candidate.action==='defer')
      return {...local,source:'local-fallback',remoteOverrideBlocked:'uncertain',jev:candidate.audit||null};
    if(!ACTIONS.includes(candidate.action)||!GOALS.includes(candidate.goal))throw new Error('Invalid Jev action or focus');
    if(number(candidate.actionConfidence)===null||candidate.actionConfidence<GATES.actionConfidence||candidate.actionConfidence>1)
      return {...local,source:'local-fallback',remoteOverrideBlocked:'uncertain',jev:candidate.audit||null};
    let blocked=null;
    if(local.action==='pause')blocked='reported_tired';
    else if(local.reasonCode==='reported_clarity'&&!['support','pause'].includes(candidate.action))blocked='reported_clarity';
    else if(candidate.action==='harder'&&(!local.evidence.upwardAllowed||number(candidate.actionProbability,0)<GATES.harderProbability))blocked='no_upward_support';
    if(blocked)return {...local,remoteOverrideBlocked:blocked,jev:candidate.audit||null};
    const p=materialize(candidate.action,local.baseLevel,candidate.goal,'jev_suggestion','jev');
    p.evidence=local.evidence;p.jev=candidate.audit||null;
    return p;
  }
  function override(plan,action) {
    const p=materialize(action,plan.baseLevel,plan.goal,'player_choice','player-choice');
    if(action==='variety'&&plan.action!=='variety')p.goal=GOALS[(GOALS.indexOf(plan.goal)+1)%GOALS.length];
    p.evidence=plan.evidence;return p;
  }
  return {VERSION,CONTRACT,ACTIONS,GOALS,REASONS,GATES,metrics,observation,learnerEstimate,stateFromGame,
    sanitizeState,summarize,hintFromText,propose,proposeState,validateRemote,override};
});
/* ALPINE_POLICY_END */
