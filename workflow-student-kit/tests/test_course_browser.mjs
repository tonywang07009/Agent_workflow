// Optional local browser smoke test. Uses a fresh profile, never the user's tabs.
import {spawn} from 'node:child_process';
import {mkdtemp, readFile, writeFile, rm, mkdir} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import path from 'node:path';
import {pathToFileURL, fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const executable=process.argv[2];
if(!executable) throw Error('Usage: node tests/test_course_browser.mjs <Chromium/Edge executable> [screenshot directory]');
const profile=await mkdtemp(path.join(tmpdir(),'workflow-browser-'));
const output=process.argv[3] ? path.resolve(process.argv[3]) : profile;
await mkdir(output,{recursive:true});
const proc=spawn(executable,['--headless=new','--disable-gpu','--no-first-run',
 '--no-default-browser-check','--remote-debugging-port=0',`--user-data-dir=${profile}`,
 '--disable-extensions','about:blank'],{windowsHide:true,stdio:'ignore'});
let socket;
try {
 let port;
 for(let i=0;i<100;i++){
  try {port=Number((await readFile(path.join(profile,'DevToolsActivePort'),'utf8')).split('\n')[0]);break;}
  catch {await new Promise(r=>setTimeout(r,100));}
 }
 assert.ok(port,'Browser did not start with a debugging port');
 const targets=await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
 const target=targets.find(t=>t.type==='page' && t.url==='about:blank');
 assert.ok(target,JSON.stringify(targets.map(t=>({type:t.type,url:t.url}))));
 socket=new WebSocket(target.webSocketDebuggerUrl);
 await new Promise((resolve,reject)=>{socket.onopen=resolve;socket.onerror=reject;});
 let seq=0;const pending=new Map();const errors=[];
 socket.onmessage=e=>{const m=JSON.parse(e.data);if(m.id){const p=pending.get(m.id);if(p){clearTimeout(p.timer);pending.delete(m.id);m.error?p.reject(Error(JSON.stringify(m.error))):p.resolve(m.result);}}
  else if(m.method==='Runtime.exceptionThrown') errors.push(m.params.exceptionDetails.text);};
 const send=(method,params={})=>new Promise((resolve,reject)=>{const id=++seq;const timer=setTimeout(()=>{pending.delete(id);reject(Error('Timed out: '+method));},10000);pending.set(id,{resolve,reject,timer});socket.send(JSON.stringify({id,method,params}));});
 const js=async expression=>{const result=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(result.exceptionDetails)throw Error(JSON.stringify(result.exceptionDetails));return result.result.value;};
 await send('Runtime.enable');await send('Page.enable');
 await send('Emulation.setDeviceMetricsOverride',{width:1440,height:1100,deviceScaleFactor:1,mobile:false});
 await send('Page.navigate',{url:pathToFileURL(path.join(root,'index.html')).href});
 for(let i=0;i<60;i++){if(await js("document.querySelectorAll('[data-lesson]').length===8"))break;await new Promise(r=>setTimeout(r,100));}
 assert.equal(await js("document.querySelectorAll('[data-lesson]').length"),8);
 assert.ok(await js('document.documentElement.scrollWidth<=window.innerWidth'),'Index horizontal overflow');
 await js("document.getElementById('start').click()");assert.equal(await js("document.querySelector('dialog').open"),true);
 await js("document.getElementById('next').click()");assert.match(await js("document.getElementById('lesson-title').textContent"),/需求/);
 await js("document.getElementById('close').click()");assert.equal(await js("document.querySelector('dialog').open"),false);
 // Verify all cards and their active reference links render.
 for(let i=0;i<8;i++){
  await js(`document.querySelector('[data-lesson="${i}"]').click()`);
  assert.ok(await js("document.querySelectorAll('#lesson-body a').length>0"));
  await js("document.getElementById('close').click()");
 }
 await writeFile(path.join(output,'index-desktop.png'),Buffer.from((await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false})).data,'base64'));
 await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
 assert.ok(await js('document.documentElement.scrollWidth<=window.innerWidth'),'Mobile index horizontal overflow');
 await send('Emulation.setDeviceMetricsOverride',{width:1440,height:1100,deviceScaleFactor:1,mobile:false});
 await send('Page.navigate',{url:pathToFileURL(path.join(root,'course/workflow.html')).href});
 for(let i=0;i<60;i++){if(await js("document.querySelectorAll('.node').length===10"))break;await new Promise(r=>setTimeout(r,100));}
 assert.equal(await js("document.querySelectorAll('.node').length"),10);
 await js("document.querySelector('[data-node=assess]').click()");
 assert.match(await js("document.getElementById('detail-points').textContent"),/筆誤直接修復/);
 await js("document.querySelector('[data-mode=auto]').click()");
 assert.match(await js("document.getElementById('mode-text').textContent"),/未決策事項/);
 await js("document.querySelector('[data-node=trial]').click()");
 assert.match(await js("document.getElementById('detail-points').textContent"),/兩個不同任務/);
 await writeFile(path.join(output,'workflow-desktop.png'),Buffer.from((await send('Page.captureScreenshot',{format:'png'})).data,'base64'));
 await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
 assert.ok(await js('document.documentElement.scrollWidth<=window.innerWidth'),'Mobile horizontal overflow');
 await writeFile(path.join(output,'workflow-mobile.png'),Buffer.from((await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true})).data,'base64'));
 assert.deepEqual(errors,[]);
 console.log(JSON.stringify({status:'PASS',cards:8,nodes:10,checks:['offline file URLs','dialogs and navigation','active references','maintenance distinction','mode demo','local stability','mobile width','no runtime exceptions'],screenshots:output}));
 await send('Browser.close').catch(()=>{});
} finally {
 if(socket)socket.close();proc.kill();
 // Verify the exact resolved temp target before recursive cleanup.
 if(path.dirname(profile)===path.resolve(tmpdir())&&path.basename(profile).startsWith('workflow-browser-')){
  await rm(profile,{recursive:true,force:true,maxRetries:10,retryDelay:150}).catch(()=>{});
 }
}
