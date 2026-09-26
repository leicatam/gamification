import json,sys,docx,re
sys.path.insert(0,'.')
from appendix_lib import Inserter
from docx.shared import Pt
R=json.load(open('audit_result.json')); O={s['section']:s for s in R['data']['appendix_outline']}
def T(sec,title_prefix):
    for t in O[sec]['tables']:
        if t['title'].startswith(title_prefix): return t
    raise KeyError(title_prefix)
d=docx.Document('V43_step2.docx')
anchor=[p for p in d.paragraphs if p.text.strip()=='Author completion checklist'][0]
ins=Inserter(d,anchor)
tno=[0]; fno=[0]
def table(title,cols,rows,widths=None,font=8.5):
    tno[0]+=1; ins.caption(f"Table I.{tno[0]}. {title}"); ins.table(cols,rows,widths,font)
def figure(path,caption,width=5.8):
    fno[0]+=1; ins.figure(path,width); ins.caption(f"Figure I.{fno[0]}. {caption}")
ins.heading('Appendix I · Stage-3B Component Study: Record at the 26 September 2026 Cut-off',2)
# I.1
ins.heading('I.1 · Status and scope',3)
ins.para("This appendix records the Stage-3B component study as it stood at a stated cut-off, 26 September 2026. It is a descriptive record, not a results chapter. The examiner-style report of 15 September 2026 on V42 stated that \"the completed thesis can present a settled account of this ongoing programme at a stated cut-off\" and that open results cells and author-input stubs should be removed if the study remains outside the evidence base; the author's decision of 26 September 2026 (recorded in the thesis repository as a dated decision note, Appendix G item G.12) took that course. After the initial round of Stage 3B, the learning measurement available in the records was not articulated to the adaptive-learning construct set out in Chapter 7 (I.6), and Stage 3B is no longer used to determine whether an adaptive-learning process occurs in the AI-enabled zero-failure game mechanism. The thesis concludes on the Stage 1–3A record; adaptive learning is carried as a design direction for discussion and future study (Chapter 7; §8.8; §9.5).")
ins.para("Three bodies of record are compiled here: the pre-specified design and its builds (I.2–I.3); the participant returns on record, verified and excluded (I.4); and a separate researcher self-test batch on the Pro v4.1 build (I.5). No confirmatory analysis is reported, no arm contrast is computed, and no cell is left open for later completion. Stage 3B was pre-specified by repository-dated records of 8–9 August 2026; it was not registered in an external registry, and the term \"pre-registered\" is not used for it. The record is stated at the cut-off: the frozen edition's clean-run window (15 September – 15 October 2026) is neither reopened nor extended here, and the thesis makes no provision for returns received after the cut-off; any such return is archived as received and could be reported only as a dated addendum outside the thesis evidence base. Nothing in this appendix feeds a result table in the main text.")
t=T('I.1 Purpose and status','Table I.1'); rows=[r[:] for r in t['rows']]
for r in rows:
    if r[0].startswith('Use as the adaptive-learning test'): r[1]="Discontinued by the author's decision of 26 September 2026 (I.6; decision note, G.12)"
    if r[0].startswith('Pro v4.1'): r[1]='Ten exports, 19–20 Sep 2026; two descriptive reports dated 20 Sep, archived as received 26 Sep; raw exports not yet deposited'
    if r[0].startswith('Clean-run returns'): r[1]='None on record at 26 Sep 2026 (window open to 15 Oct 2026; see I.1)'
table('Status of the Stage-3B record at the 26 September 2026 cut-off.',t['columns'],rows,[1.9,3.0,1.6])
# I.2
ins.heading('I.2 · Design as pre-specified (repository-dated 8–9 August 2026)',3)
c=O['I.2 Design as pre-specified']['content']
c=c.replace("persisted in the participant's browser storage, so that a participant who returns to the same browser keeps the same cell","persisted in the participant's browser storage (effectively per browser profile), so that a participant who returns in the same browser keeps the same cell while a fresh browser context would draw again")
ins.para(c)
t=T('I.2 Design as pre-specified','Table I.2')
table('Stage-3B build parameters as coded in the frozen study edition (Alpine3B_STUDY_DEV1_FROZEN_2026-09-15.html; SHA-256 in CHECKSUMS.txt).',['Parameter','Value in the build','Source (frozen DEV1 file line / record)'],t['rows'],[1.5,3.4,1.6],8)
# I.3
ins.heading('I.3 · Build and distribution lineage',3)
c=O['I.3 Build and distribution lineage']['content']
ins.para(c)
t=T('I.3 Build and distribution lineage','Table I.3'); rows=[r[:] for r in t['rows']]
for r in rows:
    if r[0].startswith('20 Aug') or r[0].startswith('20 Sep'):
        r[1]='reports dated 20 Sep 2026; archived as received 26 Sep 2026 (commit 2dec262)'
    if r[0].startswith('26 Sep'):
        r[1]='cut-off; decision note (G.12)'
table('Build and distribution lineage, 8 August – 26 September 2026 (dates UTC from the repository log; exposure only as recorded).',t['columns'],rows,[0.9,1.3,2.0,1.3,1.0],7.5)
f=O['I.3 Build and distribution lineage']['figures'][0]
figure('figs/fig_I_3.png',f['caption'],6.0)
# I.4
ins.heading('I.4 · Returns on record',3)
c=O['I.4 Returns on record']['content']
c=c.replace("; the questionnaire responses were D1 = 2, D2 = 1, F1 = 2, F2 = 2.",". The four-item questionnaire was completed; as a single return in one cell it supports no contrast and its item values are not reported here.")
c=c.replace("Because it is a single return in one cell, it supports no contrast. ","")
ins.para(c)
t=T('I.4 Returns on record','Table I.4')
cols=['Code','Received','Edition (build)','Device copy','Arm / failure mode','Provenance','Status']
rows=[]
for r in t['rows']:
    code,rec,ed,dev,arm,sess,prov,st=r
    if code=='B9V8YA': rows.append([code,rec,ed,dev,arm,prov,'Verified (checks pass); one 30-s run, questionnaire complete; pilot on an earlier sub-edition; not poolable with the frozen run'])
    elif code.startswith('Clean run'): rows.append([code,rec,ed,dev,arm,prov,st])
    else: rows.append([code,rec,ed,dev,arm,prov.replace('as above; file arrived with a personal name (to be stripped)','as above; file name carried a personal name (to be stripped from the archive copy)'),'EXCLUDED: 13-Aug edition, not the deployed build; researcher-solicited plays within ~20 min on one copy; all arm A'])
table('Stage-3B participant returns on record at 26 September 2026 (codes only; no names; no outcome values for excluded returns).',cols,rows,[0.75,1.0,1.2,0.6,0.7,1.35,1.4],7.5)
# I.5
ins.heading('I.5 · Stage-3B Pro v4.1 researcher self-test, Batch 01 (19–20 September 2026)',3)
c=O['I.5 Stage 3B Pro v4.1 self-test, Batch 01']['content']
# split into paragraphs at sensible points
parts=re.split(r'(?<=\.) (?=Batch 01 comprises|Five opening–closing|Where the two reports differ|Both reports state)',c)
for ptxt in parts: ins.para(ptxt)
S=O['I.5 Stage 3B Pro v4.1 self-test, Batch 01']
t=T('I.5 Stage 3B Pro v4.1 self-test, Batch 01','Table I.5'); table('Batch 01 deduplicated units (as stated in the Batch 01 Research Review of 20 September 2026).',t['columns'],t['rows'],[1.8,1.8,2.9])
t=T('I.5 Stage 3B Pro v4.1 self-test, Batch 01','Table I.6'); table('Record-level coverage per stored code (Batch 01).',t['columns'],t['rows'])
t=T('I.5 Stage 3B Pro v4.1 self-test, Batch 01','Table I.6a'); table('Visit-by-visit routes (W = warm-up; Pre/Post = opening/closing fixed-course check; P = practice). The Research Review states that these records must not be treated as completed adaptive-learning sequences.',t['columns'],t['rows'],[0.8,0.5,1.2,1.7,1.1,1.2])
t=T('I.5 Stage 3B Pro v4.1 self-test, Batch 01','Table I.7'); table('Decision audit: the ten feedback → proposal → applied-settings chains (two stored codes; transition numbers are exported Session_No values, which include warm-ups and checks; pace values are multipliers).',t['columns'],t['rows'],[1.0,1.3,1.2,1.1,0.9,0.6],7.5)
figure('figs/fig_I_2.png',S['figures'][1]['caption'],5.6)
t=T('I.5 Stage 3B Pro v4.1 self-test, Batch 01','Table I.8'); table('Paired fixed-course checks (opening → closing, within visit; pace ×0.85, 20 obstacles, 30-s planned duration, same input mode within each pair; course forms differ within each pair).',t['columns'],t['rows'])
figure('figs/fig_I_1.png',S['figures'][0]['caption'],5.4)
t=T('I.5 Stage 3B Pro v4.1 self-test, Batch 01','Table I.9'); table('First-visit questionnaire, one record per stored code (five-point scale, strongly disagree to strongly agree; as-administered wording from the deposited Pro v4.1 HTML).',t['columns'],t['rows'],[0.4,2.6,0.9,0.6,0.6,0.9])
t=T('I.5 Stage 3B Pro v4.1 self-test, Batch 01','Table I.10'); table('Exploratory paired statistics reproduced from the Learning Measurement addendum (conditional calculations; assumptions not verified; not confirmatory evidence of an effect or of its absence).',t['columns'],t['rows'],[2.0,1.8,2.7])
# I.6
ins.heading('I.6 · Why the learning measurement was not articulated to adaptive learning, and what a later study needs',3)
c=O['I.6 Why the learning measurement was not articulated to adaptive learning, and what a later study needs']['content']
c=c.replace("Fifth, the unit of randomisation in the study build is the participant at first enrolment in one browser, and the software edition differs","Fifth, assignment in the study build is drawn per participant at first enrolment and persisted per browser profile, and the software edition differs")
parts=re.split(r'(?<=\.) (?=A later, separately specified)',c)
for ptxt in parts: ins.para(ptxt)
t=T('I.6 Why the learning measurement was not articulated to adaptive learning, and what a later study needs','Table I.11'); table('Gap between the recorded measurement and the adaptive-learning construct.',t['columns'],t['rows'],[1.7,2.9,1.9])
# I.7
ins.heading('I.7 · Ethics, scope and outstanding author records',3)
c=O['I.7 Ethics and scope note']['content']
c=c.replace("The ethics-scope gate for Stage 3B was closed in the working record on the basis that the approval period covers the window and the memo carries no completion or no-new-collection statement; the examiner's report asks that the scope be verified against the approved protocol or an amendment and observes that \"the chronology alone proves neither approval nor non-approval\"; the thesis reports this as the state of the record.",
 "The ethics-scope gate for Stage 3B was closed in the working record on the basis that the approval period covers the window and the memo carries no completion or no-new-collection statement. The submitted application's Part B, however, states that \"the remaining activities are documentary and analytical; no new experimental deployment is planned within this project\", and the examiner's report asks that the scope be verified against the approved protocol or an amendment, observing that \"the chronology alone proves neither approval nor non-approval\". Whether the Stage-3B collection falls within the approved scope or requires an amendment is therefore recorded as an open item of the ethics record (§3.4), and no clarification or amendment is on file at the cut-off.")
c=c.replace("the two reports themselves are on disk as received but uncommitted","the two reports themselves are archived as received (26 September 2026; item G.13)")
parts=re.split(r'(?<=\.) (?=What remains an author record\.)',c)
ins.para(parts[0])
if len(parts)>1: ins.para(parts[1])
ins.para("Outstanding deposits and author records at the cut-off (tracked in the working file, entry A15): the ten raw Batch 01 exports with their SHA-256 list, the derived logbook and analysis workbooks and the extraction scripts named in the two reports; the v4.1.1 build file behind the four P8P2Z9 visit-4 runs and the remaining Pro v4.1 package files; a dated self-test roster stating which stored code was played in which role and on which device, with the consent basis for those sessions; a dated statement of how many distributor tags were issued, to how many distributors and on which dates (the tag-to-distributor list itself stays outside the archive); a clean-run log at the cut-off, including a dated statement that no return was received; the supervisor's protocol sign-off record for Stage 3B, or a dated statement of what was agreed instead; the institutional clarification of Stage-3B scope described above; and the renamed archive copies of the two excluded returns whose file names carry personal names.")
d.save('V43_step3.docx'); print('appendix built: tables',tno[0],'figures',fno[0])
