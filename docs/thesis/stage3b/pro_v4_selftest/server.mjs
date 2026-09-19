import http from 'node:http';
import { readFile } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { evaluate, JevError, policy } from './jev.mjs';
const GAME='Alpine3B_PRO_v4.0_SELFTEST.html';
const GAME_PATH=fileURLToPath(new URL(GAME,import.meta.url));

export function createGameServer({apiKey=process.env.TYPESAFE_API_KEY||'',model=process.env.JEV_MODEL||'jev-latest',evaluator=evaluate}={}) {
  let inFlight=0;
  const configured=Boolean(apiKey.trim())&&!apiKey.startsWith('replace_');
  const server=http.createServer(async(req,res)=>{
    const port=server.address()?.port;
    const allowedHosts=new Set([`127.0.0.1:${port}`,`localhost:${port}`,`[::1]:${port}`]);
    const host=req.headers.host;
    const send=(status,data)=>{if(!res.destroyed){res.writeHead(status,{'Content-Type':'application/json; charset=utf-8','Cache-Control':'no-store','X-Content-Type-Options':'nosniff'});res.end(JSON.stringify(data));}};
    if(!allowedHosts.has(host)){send(403,{error:'invalid_host'});return;}
    let pathname;
    try{pathname=new URL(req.url,`http://${host}`).pathname;}catch{send(400,{error:'invalid_url'});return;}
    if(req.method==='GET'&&pathname==='/api/health'){
      send(200,{contract:policy.CONTRACT,provider:'typesafe',configured,model,mode:'researcher-self-test',liveVerification:'not_asserted'});return;
    }
    if(req.method==='GET'&&(pathname==='/'||pathname===`/${GAME}`)){
      try{
        const html=await readFile(GAME_PATH);
        res.writeHead(200,{'Content-Type':'text/html; charset=utf-8','Cache-Control':'no-store','X-Content-Type-Options':'nosniff',
          'Referrer-Policy':'no-referrer','Content-Security-Policy':"default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; media-src 'self' blob:; object-src 'none'; base-uri 'none'; frame-ancestors 'none'"});
        res.end(html);
      }catch{send(500,{error:'game_file_missing'});}return;
    }
    if(req.method==='GET'&&pathname==='/favicon.ico'){res.writeHead(204);res.end();return;}
    if(pathname!=='/api/adapt'){send(404,{error:'not_found'});return;}
    if(req.method!=='POST'){send(405,{error:'method_not_allowed'});return;}
    // Local self-test server only: do not expose a paid inference endpoint to other web origins.
    if(req.headers.origin!==`http://${host}`||req.headers['sec-fetch-site']==='cross-site'){
      send(403,{error:'same_origin_required'});return;
    }
    if(!String(req.headers['content-type']||'').startsWith('application/json')){send(415,{error:'json_required'});return;}
    if(!configured){send(503,{error:'not_configured'});return;}
    if(inFlight>=2){send(429,{error:'busy'});return;}
    const controller=new AbortController();
    res.on('close',()=>{if(!res.writableFinished)controller.abort();});
    inFlight++;
    try{
      const chunks=[];let size=0;
      for await(const chunk of req){size+=chunk.length;if(size>24000)throw new JevError('request_too_large',413);chunks.push(chunk);}
      let body;try{body=JSON.parse(Buffer.concat(chunks).toString('utf8'));}catch{throw new JevError('invalid_json',400);}
      const result=await evaluator(body,{apiKey,model,signal:controller.signal});
      send(200,result);
    }catch(e){send(e instanceof JevError?e.status:500,{error:e instanceof JevError?e.code:'adaptation_unavailable'});}
    finally{inFlight--;}
  });
  server.requestTimeout=10000;server.headersTimeout=10000;
  return server;
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
  const port=Number(process.env.ALPINE_PORT||8787);
  if(!Number.isInteger(port)||port<1||port>65535)throw new Error('ALPINE_PORT must be a valid port number');
  const server=createGameServer();
  server.listen(port,'127.0.0.1',()=>{
    console.log(`Alpine Pro self-test: http://127.0.0.1:${port}`);
    console.log(process.env.TYPESAFE_API_KEY&&!process.env.TYPESAFE_API_KEY.startsWith('replace_')?'Jev key configured. Live inference occurs only when selected after a run.':'Jev key not configured. The game remains fully playable with offline rules.');
  });
}
