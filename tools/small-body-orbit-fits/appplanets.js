// app positions (AU, heliocentric J2000 ecliptic) of Venus, Earth, Mars, Jupiter at the JDs in argv[2] (JSON); writes argv[3]
const fs=require('fs'),s=fs.readFileSync(process.env.SSE_HTML||require('path').join(__dirname,'..','..','index.html'),'utf8');
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);return s.slice(i,j)};
eval((s.match(/^const AU=.*$/m)[0]+'\n'+grab('const EL=','\nconst SB=')+'\n'+grab('const wrapPi=','\nconst nowJD')).replace(/(^|\n)const /g,'$1var ').replace(/(^|\n)let /g,'$1var '));
var byId={earth:{id:'earth',orb:'em'}};const T=JSON.parse(fs.readFileSync(process.argv[2])),A=[0,0,0],out={};
for(const p of['venus','earth','mars','jupiter']){const o=p==='earth'?byId.earth:{id:p,orb:'pl'};out[p]=T.map(t=>{helio(o,t,A);return[A[0]/AU,A[1]/AU,A[2]/AU]})}
fs.writeFileSync(process.argv[3],JSON.stringify(out));
