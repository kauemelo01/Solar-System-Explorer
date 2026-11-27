// The app's own planet code (index.html with data/planet-orbits.js) against Horizons at the test dates (node hz.js check / far), and the same for
// Standish's elements: largest and rms error seen from the Sun and from the Earth-Moon barycentre, and the step ratio at every window boundary.
// node validate.js [check|far]
const fs=require('fs'),path=require('path'),{D}=require('./hz.js');
const H=process.env.SSE_HTML||path.join(__dirname,'..','..','index.html'),s=fs.readFileSync(H,'utf8'),tag=process.argv[2]||'check';
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);return s.slice(i,j)};
const window={};eval(fs.readFileSync(H.replace('index.html','data/planet-orbits.js'),'utf8'));
eval((s.match(/^const AU=.*$/m)[0]+'\n'+grab('const EL=','\nconst SB=')+'\n'+grab('const wrapPi=','\nconst nowJD')).replace(/(^|\n)const /g,'$1var ').replace(/(^|\n)let /g,'$1var '));
const IDS=['mercury','venus','emb','mars','jupiter','saturn','uranus','neptune','pluto'],A=[0,0,0],B=[0,0,0];
const pos=(k,jd,std)=>{(std?kep(EL[k],jd,A):plHelio(k,jd,A));return[A[0]/AU,A[1]/AU,A[2]/AU]};
const ang=(p,q)=>Math.acos(Math.max(-1,Math.min(1,(p[0]*q[0]+p[1]*q[1]+p[2]*q[2])/Math.hypot(...p)/Math.hypot(...q))))/DEG*3600;
const E={};for(const r of JSON.parse(fs.readFileSync(`${D}/emb-${tag}.json`)))E[r[0]]=r;
const f=x=>x>=100?x.toFixed(0):x.toFixed(1);
console.log(`${tag==='far'?'1600-1800 and 2051-2250 (extrapolated)':'1800-2050, test dates not used in the fit'}: error in arcseconds (" ), fit vs Standish`);
console.log('body       dates  from Sun: max    rms   | Standish max    rms  | from Earth: max   rms  | Standish max   rms  | km max (fit)');
for(const k of IDS){const R=JSON.parse(fs.readFileSync(`${D}/${k}-${tag}.json`));const st={};for(const std of[0,1]){let mx=0,ss=0,gm=0,gs=0,km=0,ng=0;
  for(const[jd,x,y,z]of R){const p=pos(k,jd,std),q=[x,y,z],a=ang(p,q);mx=Math.max(mx,a);ss+=a*a;km=Math.max(km,Math.hypot(p[0]-x,p[1]-y,p[2]-z)*149597870.7);
   const e=E[jd];if(k!=='emb'&&e){const pe=pos('emb',jd,std),g=ang([p[0]-pe[0],p[1]-pe[1],p[2]-pe[2]],[x-e[1],y-e[2],z-e[3]]);gm=Math.max(gm,g);gs+=g*g;ng++}}
  st[std]=[mx,Math.sqrt(ss/R.length),gm,ng?Math.sqrt(gs/ng):0,km]}
 const[a,b]=[st[0],st[1]];console.log(`${k.padEnd(9)} ${String(R.length).padStart(6)}   ${f(a[0]).padStart(10)} ${f(a[1]).padStart(6)}   | ${f(b[0]).padStart(12)} ${f(b[1]).padStart(6)} | ${k==='emb'?'         —      —  |            —     — ':`${f(a[2]).padStart(14)} ${f(a[3]).padStart(5)}  | ${f(b[2]).padStart(12)} ${f(b[3]).padStart(5)} `} | ${a[4].toFixed(0).padStart(9)}`)}
if(tag==='check'){let worst=[0];for(const k of IDS){const W=window.PL_FIT[k],P=t=>{plHelio(k,t,B);return[B[0],B[1],B[2]]};
  for(let i=1;i<W.length;i++){const t=W[i][0]+J2000,h=Math.min(W[i][1]-W[i][0],W[i-1][1]-W[i-1][0])*1e-4,p=[-2,-1,0,1,2].map(x=>P(t+x*h)),
   st=q=>Math.hypot(p[q+1][0]-p[q][0],p[q+1][1]-p[q][1],p[q+1][2]-p[q][2]),r=Math.max(st(1),st(2))/Math.min(st(0),st(3));if(r>worst[0])worst=[r,k,t]}}
 console.log(`window boundaries: largest step ratio ${worst[0].toFixed(4)} (${worst[1]}, JD ${worst[2].toFixed(1)}); 1 = perfectly smooth`)}
