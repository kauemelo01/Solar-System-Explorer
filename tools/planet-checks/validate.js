// The app's planets, Earth-Moon barycentre and Pluto (plHelio() in index.html: Standish and Williams's Table 1 over 1800-2050, Table 2 outside, blended over 30 years)
// against JPL Horizons (node hz.js check, far and wide first), next to Table 1 alone and Table 2 alone: the largest error in arcseconds, seen from the Sun and from the
// Earth-Moon barycentre, in each span of years. Then: the smoothness of the blends, that the app is exactly Table 1 over 1800-2050, and how much of the inner
// planets' error before 1600 is the app's use of Universal Time for Terrestrial Time.
// node validate.js                 BINS='[[1000,1800],[1800,2051],[2051,3000]]' node validate.js     FADE=100 node validate.js (another blend length, in years)
const fs=require('fs'),path=require('path'),{D}=require('./hz.js');
const H=process.env.SSE_HTML||path.join(__dirname,'..','..','index.html'),s=fs.readFileSync(H,'utf8');
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);if(i<0||j<0)throw new Error('not found in index.html: '+a);return s.slice(i,j)};
eval((s.match(/^const AU=.*$/m)[0]+'\n'+grab('const EL=','\nconst SB=')+'\n'+grab('const wrapPi=','\nconst nowJD')).replace(/(^|\n)const /g,'$1var ').replace(/(^|\n)let /g,'$1var '));
if(process.env.FADE)PL_FADE=process.env.FADE*365.25;
const IDS=['mercury','venus','emb','mars','jupiter','saturn','uranus','neptune','pluto'],A=[0,0,0];
const M={app:(k,jd)=>plHelio(k,jd,A),t1:(k,jd)=>kep(EL[k],jd,A),t2:(k,jd)=>kep(EL2[k],jd,A)};
const pos=(m,k,jd)=>{M[m](k,jd);return[A[0]/AU,A[1]/AU,A[2]/AU]};
const ang=(p,q)=>Math.acos(Math.max(-1,Math.min(1,(p[0]*q[0]+p[1]*q[1]+p[2]*q[2])/Math.hypot(...p)/Math.hypot(...q))))/DEG*3600;
const yr=jd=>2000+(jd-2451545)/365.25;
const BINS=process.env.BINS?JSON.parse(process.env.BINS):[[1000,1600],[1600,1770],[1770,1800],[1800,2051],[2051,2081],[2081,2250],[2250,3000]];
const rows={};for(const k of IDS){rows[k]=[];for(const t of['wide','far','check'])rows[k]=rows[k].concat(JSON.parse(fs.readFileSync(`${D}/${k}-${t}.json`)))}
const E={};for(const r of rows.emb)E[r[0]]=r;
const f=x=>x>=100?x.toFixed(0):x.toFixed(1);
for(const geo of[0,1]){console.log(`\nlargest error ${geo?'seen from the Earth-Moon barycentre':'seen from the Sun'} (arcsec): app / Table 1 alone / Table 2 alone`);
 console.log('body     '+BINS.map(b=>`${b[0]}-${b[1]}`.padStart(19)).join(''));
 for(const k of IDS){if(geo&&k==='emb')continue;const out=BINS.map(()=>({app:0,t1:0,t2:0,n:0}));
  for(const[jd,x,y,z]of rows[k]){const b=BINS.findIndex(([a,c])=>yr(jd)>=a&&yr(jd)<c);if(b<0)continue;const e=E[jd];if(geo&&!e)continue;out[b].n++;
   for(const m of['app','t1','t2']){let p=pos(m,k,jd),q=[x,y,z];if(geo){const pe=pos(m,'emb',jd);p=[p[0]-pe[0],p[1]-pe[1],p[2]-pe[2]];q=[x-e[1],y-e[2],z-e[3]]}out[b][m]=Math.max(out[b][m],ang(p,q))}}
  console.log(k.padEnd(9)+out.map(o=>o.n?`${f(o.app)}/${f(o.t1)}/${f(o.t2)}`.padStart(19):'—'.padStart(19)).join(''))}}
// blends: the step ratio over 1-day steps (largest of the two middle steps over the smaller outer one), against Table 1 alone, every 5 days through each blend
const ratio=(m,k,t)=>{const p=[-2,-1,0,1,2].map(x=>pos(m,k,t+x)),st=q=>Math.hypot(p[q+1][0]-p[q][0],p[q+1][1]-p[q][1],p[q+1][2]-p[q][2]);return Math.max(st(1),st(2))/Math.min(st(0),st(3))};
let worst=[0];for(const k of IDS)for(const[a,b]of[[PL_T1A-PL_FADE,PL_T1A],[PL_T1B,PL_T1B+PL_FADE]])for(let t=a-20;t<=b+20;t+=5){const r=ratio('app',k,t)/ratio('t1',k,t);if(r>worst[0])worst=[r,k,yr(t).toFixed(2)]}
console.log(`\nblends: largest 1-day step ratio against Table 1 alone ${worst[0].toFixed(6)} (${worst[1]}, ${worst[2]}); 1 = as smooth as Table 1`);
let diff=0;for(const k of IDS)for(let jd=PL_T1A;jd<=PL_T1B;jd+=7.3){M.app(k,jd);const a=[...A];M.t1(k,jd);diff=Math.max(diff,Math.abs(a[0]-A[0]),Math.abs(a[1]-A[1]),Math.abs(a[2]-A[2]))}
console.log('1800-2050: largest difference from Table 1 alone',diff,'(0 = Table 1 unchanged)');
// Universal Time vs Terrestrial Time before 1600: Delta T from the Espenak-Meeus polynomial for 500-1600 AD
const dT=y=>{const u=(y-1000)/100;return 1574.2-556.01*u+71.23472*u*u+0.319781*u**3-0.8503463*u**4-0.005050998*u**5+0.0083572073*u**6};
console.log('\n1000-1600, seen from the Sun, the app as it is / with Delta T applied (arcsec):');
for(const k of['mercury','venus','emb']){let m0=0,m1=0;for(const[jd,x,y,z]of rows[k]){const y_=yr(jd);if(y_>=1600)continue;
  m0=Math.max(m0,ang(pos('app',k,jd),[x,y,z]));m1=Math.max(m1,ang(pos('app',k,jd+dT(y_)/86400),[x,y,z]))}console.log(`${k.padEnd(9)}${f(m0).padStart(7)} /${f(m1).padStart(6)}`)}
