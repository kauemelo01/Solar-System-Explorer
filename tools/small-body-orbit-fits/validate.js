// The app's own code, with data/sb-orbits.js, against Horizons samples: the 1-deg-or-1-day target at every sample.
// node validate.js <samples dir> [ids...]; samples: <dir>/<id>.json rows [jd,x,y,z,vx,vy,vz] (AU, AU/d, helio J2000 ecliptic, UT)
const fs=require('fs'),H=process.env.SSE_HTML||require('path').join(__dirname,'..','..','index.html'),s=fs.readFileSync(H,'utf8');
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);return s.slice(i,j)};
const window={};eval(fs.readFileSync(H.replace('index.html','data/sb-orbits.js'),'utf8'));eval(fs.readFileSync(H.replace('index.html','data/planet-orbits.js'),'utf8'));
eval((s.match(/^const AU=.*$/m)[0]+'\n'+grab('const EL=','\nconst SB=')+'\n'+grab('const wrapPi=','\nconst nowJD')).replace(/(^|\n)const /g,'$1var ').replace(/(^|\n)let /g,'$1var '));
const i0=s.indexOf('const SB=');let d=0,j=i0+9;for(;j<s.length;j++){if(s[j]=='[')d++;else if(s[j]==']'){d--;if(!d)break}}
const SBl=eval(s.slice(i0+9,j+1));var byId={};const dir=process.argv[2],want=process.argv.slice(3),A=[0,0,0],out={};
for(const[id,name,,,a,e,i,om,w,M0,ep]of SBl){if(want.length&&!want.includes(id))continue;const f=dir+'/'+id+'.json';if(!fs.existsSync(f))continue;
 const[Pv,Qv]=PQ(om,i,w),W=window.SB_FIT[id],o={orb:'sb',a:a*AU,b:a*AU*Math.sqrt(1-e*e),e,M0,ep,n:0.9856076686/Math.pow(a,1.5),Pv,Qv,fit:W?{w:W,sb:1}:null};
 let bad=0,n=0,worstA=0,worstT=0,firstBad=null;
 for(const[jd,x,y,z,vx,vy,vz]of JSON.parse(fs.readFileSync(f))){helio(o,jd,A);const p=[A[0]/AU,A[1]/AU,A[2]/AU],r=Math.hypot(x,y,z),res=[p[0]-x,p[1]-y,p[2]-z];
  const ang=Math.acos(Math.max(-1,Math.min(1,(p[0]*x+p[1]*y+p[2]*z)/Math.hypot(...p)/r)))/DEG,vn=Math.hypot(vx,vy,vz),along=(res[0]*vx+res[1]*vy+res[2]*vz)/vn;
  const perp=Math.hypot(res[0]-along*vx/vn,res[1]-along*vy/vn,res[2]-along*vz/vn)/r/DEG,dt=Math.abs(along)/vn;
  const ok=ang<=1||(perp<=1&&dt<=1);n++;if(!ok){bad++;if(!firstBad)firstBad=jd}worstA=Math.max(worstA,ang);worstT=Math.max(worstT,Math.min(dt,1e9))}
 out[id]={name,n,bad,worstA,firstBad,windows:W?W.length:0};
 console.log(`${bad?'FAIL':'pass'} ${name.padEnd(27)} ${String(W?W.length:0).padStart(4)} windows  ${n} test dates  worst angle ${worstA.toFixed(3)}°${bad?`  ${bad} dates miss (first JD ${firstBad.toFixed(2)})`:''}`)}
fs.writeFileSync(dir+'/../validate_out.json',JSON.stringify(out));
