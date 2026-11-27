// app positions of the small bodies' moons relative to their primary (km, J2000 ecliptic), from index.html
const fs=require('fs'),H=require('path').join(__dirname,'..','..','..','index.html'),s=fs.readFileSync(H,'utf8');
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);return s.slice(i,j)};
eval((s.match(/^const AU=.*$/m)[0]+'\n'+grab('const EL=','\nconst SB=')+'\n'+grab('const wrapPi=','\nconst nowJD')).replace(/(^|\n)const /g,'$1var ').replace(/(^|\n)let /g,'$1var '));
const MO=JSON.parse(s.slice(s.indexOf('const MOONS=')+12,s.indexOf(';\n',s.indexOf('const MOONS='))));
eval(s.match(/const MOON_EP=\{[^}]*\};/)[0].replace('const ','var '));
const window={};eval(fs.readFileSync(H.replace('index.html','data/sb-orbits.js'),'utf8'));eval(fs.readFileSync(H.replace('index.html','data/planet-orbits.js'),'utf8'));const FIT=window.SBM_FIT;
module.exports=function(name){const r=MO.find(m=>m[0]===name);const[nm,pid,akm,e,w,M0,inc,node,P,ra,dec,fam]=r;const[Pv,Qv]=PQ(node,inc,w,ra,dec);
 const o={a:akm*KM,b:akm*KM*Math.sqrt(1-e*e),e,M0,ep:MOON_EP[nm]||J2000,n:360/P,Pv,Qv,fit:FIT[nm]||null};const A=[0,0,0];
 return {P,pid,pos:jd=>{ell(o,jd,A);return[A[0]/KM,A[1]/KM,A[2]/KM]}}};
