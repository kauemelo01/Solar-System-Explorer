// Smoothness check: sample each windowed moon like a 250-year trail held on its planet; find sharp direction changes (turn angle far from its neighbours)
const fs=require('fs'),html=process.argv[2],data=process.argv[3],only=process.argv[4],s=fs.readFileSync(html,'utf8');
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);return s.slice(i,j)};
const code=s.match(/^const AU=.*$/m)[0]+'\n'+grab('const wrapPi=','\nconst eqToEcl')+'\n'+s.match(/^const eqToEcl=.*$/m)[0]+'\n'+grab('function PQ(','function kep(')+'\n'+grab('const _mo=','const MU=');
const window={};eval(fs.readFileSync(data,'utf8'));eval(code.replace(/(^|\n)const /g,'$1var '));
const MO=(()=>{const i=s.indexOf('const MOONS='),j=s.indexOf(';\n',i);return JSON.parse(s.slice(i+12,j))})(),P={};for(const r of MO)P[r[0]]=r[8];
const J=2451545,res=[];
for(const name in window.MOON_FIT){if(only&&name!==only)continue;const fit=window.MOON_FIT[name];if(!fit.w)continue;const o={fit,a:0,e:0,inc:0};
 const step=P[name]/180,t0=fit.t[0],t1=fit.t[1],pts=[];for(let t=t0;t<=t1;t+=step){const v=[0,0,0];ell(o,J+t,v);pts.push([t,v])}
 const turn=[];for(let i=1;i<pts.length-1;i++){const a=pts[i-1][1],b=pts[i][1],c=pts[i+1][1],u=[b[0]-a[0],b[1]-a[1],b[2]-a[2]],w=[c[0]-b[0],c[1]-b[1],c[2]-b[2]];
  const cs=(u[0]*w[0]+u[1]*w[1]+u[2]*w[2])/Math.hypot(...u)/Math.hypot(...w);turn.push([pts[i][0],Math.acos(Math.max(-1,Math.min(1,cs)))*180/Math.PI])}
 let worst=0,wt=0,cnt=0;for(let i=3;i<turn.length-3;i++){const nb=[turn[i-3][1],turn[i-2][1],turn[i+2][1],turn[i+3][1]].sort((x,y)=>x-y),ref=(nb[1]+nb[2])/2,d=turn[i][1]-ref;
  if(d>worst){worst=d;wt=turn[i][0]}if(d>Math.max(1,ref))cnt++}
 res.push([name,worst,cnt,(2000+wt/365.25).toFixed(1)])}
res.sort((a,b)=>b[1]-a[1]);console.log(res.slice(0,only?1:25).map(r=>`${r[0]}: worst extra bend ${r[1].toFixed(1)}° in ${r[3]}, sharp bends ${r[2]}`).join('\n'));
console.log('moons with an extra bend > 5°:',res.filter(r=>r[1]>5).length,'of',res.length);
