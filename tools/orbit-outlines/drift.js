// Which bodies get an orbit outline (docs/sources.md#orbit-outlines): the orbit the app uses for a body on a date, held fixed, must stay
// within LIMIT degrees of the body (seen from the Sun) for the next 30 years, from every start date 1800, 1820, ..., 2020. Long-period
// comets (period over 200 years), whose orbit is known for one pass near the Sun only, are left out. The app's own code (index.html,
// data/sb-orbits.js) gives both the orbit and the body's positions; the result is compared with OUTLINED in index.html.
// node drift.js [limit in degrees, default 0.3]
const fs=require('fs'),path=require('path'),R=path.join(__dirname,'..','..'),s=fs.readFileSync(path.join(R,'index.html'),'utf8');
const LIMIT=+(process.argv[2]||0.3),YEARS=30,STARTS=[];for(let y=1800;y<=2020;y+=20)STARTS.push(y);
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);if(i<0||j<0)throw new Error('not found in index.html: '+a);return s.slice(i,j)};
var window={};eval(fs.readFileSync(path.join(R,'data','sb-orbits.js'),'utf8'));
eval((s.match(/^const AU=.*$/m)[0]+'\n'+grab('const EL=','\nconst SB=')+'\n'+grab('const wrapPi=','\nconst nowJD')).replace(/(^|\n)const /g,'$1var ').replace(/(^|\n)let /g,'$1var '));
const i0=s.indexOf('const SB=');let d=0,j=i0+9;for(;j<s.length;j++){if(s[j]=='[')d++;else if(s[j]==']'){d--;if(!d)break}}const SBl=eval(s.slice(i0+9,j+1));
const OUTLINED=eval(s.match(/^const OUTLINED=(\[[\s\S]*?\]);/m)[1]);
const yr=y=>J2000+(y-2000)*365.25,A=[0,0,0],B=[0,0,0];
// distance from a point to an ellipse (in its plane: a(cos E - e), b sin E; P, Q, and the normal W): the nearest E by a coarse scan and a golden-section search
function offEllipse(p,P,Q,a,b,e){const W=[P[1]*Q[2]-P[2]*Q[1],P[2]*Q[0]-P[0]*Q[2],P[0]*Q[1]-P[1]*Q[0]],x=p[0]*P[0]+p[1]*P[1]+p[2]*P[2],y=p[0]*Q[0]+p[1]*Q[1]+p[2]*Q[2],z=p[0]*W[0]+p[1]*W[1]+p[2]*W[2];
 const D=E=>Math.hypot(a*(Math.cos(E)-e)-x,b*Math.sin(E)-y);let bE=0,bd=Infinity;for(let k=0;k<64;k++){const E=k/64*TAU,dd=D(E);if(dd<bd){bd=dd;bE=E}}
 let lo=bE-TAU/64,hi=bE+TAU/64;for(let it=0;it<40;it++){const m1=lo+(hi-lo)*.382,m2=lo+(hi-lo)*.618;if(D(m1)<D(m2))hi=m2;else lo=m1}return Math.hypot(D((lo+hi)/2),z)}
const rows=[];
// planets and Pluto: their elements at t0 held fixed (the mean longitude still moves); the body from plHelio
for(const k of['mercury','venus','emb','mars','jupiter','saturn','uranus','neptune','pluto']){let worst=0;
 for(const y0 of STARTS){const t0=yr(y0),el=EL[k],T=(t0-J2000)/36525,fz=[el[0]+el[6]*T,el[1]+el[7]*T,el[2]+el[8]*T,el[3],el[4]+el[10]*T,el[5]+el[11]*T,0,0,0,el[9],0,0];
  for(let t=t0;t<=t0+YEARS*365.25;t+=5){plHelio(k,t,A);const D=x=>{kep(fz,x,B);return Math.hypot(A[0]-B[0],A[1]-B[1],A[2]-B[2])};let lo=t-30,hi=t+30;
   for(let it=0;it<60;it++){const m1=lo+(hi-lo)*.382,m2=lo+(hi-lo)*.618;if(D(m1)<D(m2))hi=m2;else lo=m1}worst=Math.max(worst,D((lo+hi)/2)/Math.hypot(...A)/DEG)}}
 rows.push({id:k==='emb'?'earth':k,name:k==='emb'?'Earth (Earth-Moon barycentre)':k[0].toUpperCase()+k.slice(1),cat:k==='pluto'?'dwarf':'planet',worst,P:0})}
// small bodies: the window the start date is in (or the one SBDB orbit) held fixed; the body from helio (blended windows)
for(const[id,name,cat,kind,a,e,i,om,w,M0,ep]of SBl){const[Pv,Qv]=PQ(om,i,w),W=window.SB_FIT[id];
 const o={id,orb:'sb',a:a*AU,b:a*AU*Math.sqrt(1-e*e),e,M0,ep,n:0.9856076686/Math.pow(a,1.5),Pv,Qv,fit:W?{w:W,sb:1}:null},P=360/o.n;let worst=0;
 for(const y0 of STARTS){const t0=yr(y0);let Pp=o.Pv,Qq=o.Qv,Aa=o.a,ee=o.e,Bb=o.b;if(o.fit){const m=moonOrbit(o,t0,winOf(W,t0-J2000));Pp=m.P.slice();Qq=m.Q.slice();Aa=m.a;ee=m.e;Bb=m.b}
  for(let t=t0;t<=t0+YEARS*365.25;t+=Math.max(1,Math.min(30,P/200))){helio(o,t,A);worst=Math.max(worst,offEllipse(A,Pp,Qq,Aa,Bb,ee)/Math.hypot(...A)/DEG)}}
 rows.push({id,name,cat:String(kind).includes('candidate')?'candidate':cat,worst,P:P/365.25})}
let bad=0;console.log(`Within ${LIMIT}° of a fixed orbit for ${YEARS} years from every start date ${STARTS[0]}-${STARTS[STARTS.length-1]}:\n`);
for(const r of rows.sort((x,y)=>x.worst-y.worst)){const long=r.cat==='comet'&&r.P>200,pass=r.worst<=LIMIT&&!long,inApp=OUTLINED.includes(r.id);if(pass!==inApp)bad++;
 console.log(`${pass?'outline':'   -   '}  ${r.name.padEnd(30)} ${r.cat.padEnd(9)} ${r.worst.toFixed(3).padStart(8)}°${long?'  (long-period comet: left out)':''}${pass!==inApp?'  <- differs from OUTLINED in index.html':''}`)}
console.log(bad?`\n${bad} bodies differ from OUTLINED in index.html`:`\nOUTLINED in index.html matches (${OUTLINED.length} bodies)`);
