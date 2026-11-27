// Each close encounter in encounters.json, in the app: does it happen, and is its closest point within 3 hours of JPL's?
const fs=require('fs'),H=process.env.SSE_HTML||require('path').join(__dirname,'..','..','index.html'),s=fs.readFileSync(H,'utf8');
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);return s.slice(i,j)};
const window={};eval(fs.readFileSync(H.replace('index.html','data/sb-orbits.js'),'utf8'));eval(fs.readFileSync(H.replace('index.html','data/planet-orbits.js'),'utf8'));
eval((s.match(/^const AU=.*$/m)[0]+'\n'+grab('const EL=','\nconst SB=')+'\n'+grab('const wrapPi=','\nconst nowJD')).replace(/(^|\n)const /g,'$1var ').replace(/(^|\n)let /g,'$1var '));
const i0=s.indexOf('const SB=');let d=0,j=i0+9;for(;j<s.length;j++){if(s[j]=='[')d++;else if(s[j]==']'){d--;if(!d)break}}
const SBl=eval(s.slice(i0+9,j+1));var byId={earth:{id:'earth',orb:'em'},moon:{id:'moon',orb:'em'}};
const PL={venus:{id:'venus',orb:'pl'},earth:byId.earth,moon:byId.moon,mars:{id:'mars',orb:'pl'},jupiter:{id:'jupiter',orb:'pl'}},LIM={venus:.05,earth:.05,moon:.05,mars:.05,jupiter:.35};
const O={};for(const[id,name,,,a,e,i,om,w,M0,ep]of SBl){const[Pv,Qv]=PQ(om,i,w),W=window.SB_FIT[id];O[id]={name,orb:'sb',a:a*AU,b:a*AU*Math.sqrt(1-e*e),e,M0,ep,n:0.9856076686/Math.pow(a,1.5),Pv,Qv,fit:W?{w:W,sb:1}:null}}
const A=[0,0,0],B=[0,0,0],KMAU=149597870.7;const dist=(o,p,t)=>{helio(o,t,A);helio(p,t,B);return Math.hypot(A[0]-B[0],A[1]-B[1],A[2]-B[2])/AU*KMAU};
const iso=jd=>new Date((jd-2440587.5)*864e5).toISOString().slice(0,16).replace('T',' ');const res=[];
for(const E of JSON.parse(fs.readFileSync(process.argv[2]))){const o=O[E.id],p=PL[E.body],W=E.body==='jupiter'?60:5;
 let best=1e18,bt=0;for(let t=E.jd-W;t<=E.jd+W;t+=W/2000){const x=dist(o,p,t);if(x<best){best=x;bt=t}}
 for(let h=W/2000;h>1e-6;h/=2)for(const t of[bt-h,bt+h]){const x=dist(o,p,t);if(x<best){best=x;bt=t}}
 const edge=Math.abs(bt-E.jd)>W*0.99,dt=(bt-E.jd)*24,ok=!edge&&best/KMAU<LIM[E.body]&&Math.abs(dt)<=3;
 res.push({...E,name:o.name,app:best,dth:dt,ok});
 console.log(`${ok?'pass':'FAIL'} ${o.name.padEnd(26)} ${E.body.padEnd(7)} ${iso(E.jd)}  JPL ${Math.round(E.km).toLocaleString('en').padStart(11)} km  app ${Math.round(best).toLocaleString('en').padStart(11)} km  ${edge?'no approach':(dt>=0?'+':'')+(Math.abs(dt)<1?(dt*60).toFixed(0)+' min':dt.toFixed(1)+' h')}`)}
console.log(`\n${res.filter(r=>r.ok).length} of ${res.length} close encounters meet the target`);fs.writeFileSync(require('path').join(require('path').dirname(process.argv[2]),'flycheck.json'),JSON.stringify(res));
