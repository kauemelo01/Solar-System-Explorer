// Evaluate data/moon-orbits.js with the app's own code (extracted from index.html) against the Horizons check series
const fs=require('fs'),[,,html,data,check]=process.argv,s=fs.readFileSync(html,'utf8');
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);if(i<0||j<0)throw a;return s.slice(i,j)};
const code=s.match(/^const AU=.*$/m)[0]+'\n'+grab('const wrapPi=','\nconst eqToEcl')+'\n'+s.match(/^const eqToEcl=.*$/m)[0]+'\n'+grab('function PQ(','function kep(')+'\n'+grab('const _mo=','const MU=');
const window={};eval(fs.readFileSync(data,'utf8'));eval(code.replace(/(^|\n)const /g,'$1var '));
const C=JSON.parse(fs.readFileSync(check,'utf8')),out={};const _o=[0,0,0];
for(const name in window.MOON_FIT){const fit=window.MOON_FIT[name],ser=C[name];if(!ser)continue;
 const o={fit,a:fit.s?fit.s[0]*KM:0,e:fit.s?fit.s[1]:0,inc:fit.s?fit.s[2]:0};o.b=o.a*Math.sqrt(1-o.e*o.e);
 let mx=0,ss=0;for(const[jd,x,y,z]of ser){ell(o,jd,_o);const c=(_o[0]*x+_o[1]*y+_o[2]*z)/Math.hypot(..._o)/Math.hypot(x,y,z),e=Math.acos(Math.max(-1,Math.min(1,c)))*180/Math.PI;mx=Math.max(mx,e);ss+=e*e}
 out[name]={kind:fit.g?'g':'w',max:+mx.toFixed(3),rms:+Math.sqrt(ss/ser.length).toFixed(3),n:ser.length}}
// baseline: the app without fits (JPL mean elements, as in Release 2)
const MO=(()=>{const i=s.indexOf('const MOONS='),j=s.indexOf(';\n',i);return JSON.parse(s.slice(i+12,j))})();
for(const r of MO){const[name,pid,akm,e,w,M0,inc,node,P,ra,dec]=r;const ser=C[name];if(!ser||!out[name])continue;const[Pv,Qv]=PQ(node,inc,w,ra,dec);
 const o={a:akm*KM,b:akm*KM*Math.sqrt(1-e*e),e,M0,ep:J2000,n:360/P,Pv,Qv};let mx=0,ss=0;
 for(const[jd,x,y,z]of ser){ell(o,jd,_o);const c=(_o[0]*x+_o[1]*y+_o[2]*z)/Math.hypot(..._o)/Math.hypot(x,y,z),q=Math.acos(Math.max(-1,Math.min(1,c)))*180/Math.PI;mx=Math.max(mx,q);ss+=q*q}
 out[name].old_max=+mx.toFixed(2);out[name].old_rms=+Math.sqrt(ss/ser.length).toFixed(2)}
fs.writeFileSync('validate.json',JSON.stringify(out));console.log('validated',Object.keys(out).length);
