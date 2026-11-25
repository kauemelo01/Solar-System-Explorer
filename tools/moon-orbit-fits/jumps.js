// Continuity check: position jump at every window boundary of every windowed moon, as a fraction of its distance from the planet
const fs=require('fs'),html=process.argv[2],data=process.argv[3],s=fs.readFileSync(html,'utf8');
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);return s.slice(i,j)};
const code=s.match(/^const AU=.*$/m)[0]+'\n'+grab('const wrapPi=','\nconst eqToEcl')+'\n'+s.match(/^const eqToEcl=.*$/m)[0]+'\n'+grab('function PQ(','function kep(')+'\n'+grab('const _mo=','const MU=');
const window={};eval(fs.readFileSync(data,'utf8'));eval(code.replace(/(^|\n)const /g,'$1var '));
const J=2451545,o0=[0,0,0],o1=[0,0,0],res=[];
for(const name in window.MOON_FIT){const fit=window.MOON_FIT[name];if(!fit.w)continue;const o={fit,a:fit.s?fit.s[0]*KM:0,e:0,inc:0};
 let worst=0,sum=0,n=0;for(let k=0;k<fit.w.length-1;k++){const tb=fit.w[k][1];
  ell(o,J+tb-0.01,o0);ell(o,J+tb+0.01,o1);const jump=Math.hypot(o1[0]-o0[0],o1[1]-o0[1],o1[2]-o0[2]),r=Math.hypot(...o0);worst=Math.max(worst,jump/r);sum+=jump/r;n++}
 res.push([name,worst,sum/n,fit.w.length])}
res.sort((a,b)=>b[1]-a[1]);
const med=a=>a.slice().sort((x,y)=>x-y)[a.length>>1];
console.log('windowed moons',res.length,'| jump at a boundary, as fraction of distance: median of moon-averages',med(res.map(r=>r[2])).toFixed(3),'| worst',res[0][1].toFixed(3));
console.log(res.slice(0,8).map(r=>r[0]+' '+r[1].toFixed(3)).join(', '));

