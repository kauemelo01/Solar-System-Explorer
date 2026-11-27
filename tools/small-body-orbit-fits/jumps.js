// at every window boundary, compare the app's step across the boundary with the steps just before and after it
const fs=require('fs'),H=process.env.SSE_HTML||require('path').join(__dirname,'..','..','index.html'),s=fs.readFileSync(H,'utf8');
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);return s.slice(i,j)};
const window={};eval(fs.readFileSync(H.replace('index.html','data/sb-orbits.js'),'utf8'));eval(fs.readFileSync(H.replace('index.html','data/planet-orbits.js'),'utf8'));
eval((s.match(/^const AU=.*$/m)[0]+'\n'+grab('const EL=','\nconst SB=')+'\n'+grab('const wrapPi=','\nconst nowJD')).replace(/(^|\n)const /g,'$1var ').replace(/(^|\n)let /g,'$1var '));
const i0=s.indexOf('const SB=');let d=0,j=i0+9;for(;j<s.length;j++){if(s[j]=='[')d++;else if(s[j]==']'){d--;if(!d)break}}
const SBl=eval(s.slice(i0+9,j+1));var byId={};const A=[0,0,0];let worst=[0];
for(const[id,name,,,a,e,i,om,w,M0,ep]of SBl){const W=window.SB_FIT[id];if(!W)continue;const[Pv,Qv]=PQ(om,i,w);
 const o={orb:'sb',a:a*AU,b:a*AU*Math.sqrt(1-e*e),e,M0,ep,n:0.9856076686/Math.pow(a,1.5),Pv,Qv,fit:{w:W,sb:1}};
 const P=t=>{helio(o,t,A);return[A[0],A[1],A[2]]};let wb=0,at=0;
 for(let k=1;k<W.length;k++){const t=W[k][0]+J2000,h=Math.min(W[k][1]-W[k][0],W[k-1][1]-W[k-1][0])*1e-4;
  const p=[-2,-1,0,1,2].map(x=>P(t+x*h)),st=q=>Math.hypot(p[q+1][0]-p[q][0],p[q+1][1]-p[q][1],p[q+1][2]-p[q][2]);
  const r=Math.max(st(1),st(2))/Math.min(st(0),st(3));if(r>wb){wb=r;at=t}}
 if(wb>worst[0])worst=[wb,name,at];if(wb>1.05)console.log(name,'step ratio',wb.toFixed(3),'at JD',at.toFixed(3))}
console.log('largest step ratio at a boundary:',worst[0].toFixed(4),worst[1]);
