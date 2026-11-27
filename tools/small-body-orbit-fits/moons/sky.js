// For each Miriade date: light-time-corrected emission time, sky basis (east, north) in J2000 ecliptic, Earth distance; and the app's moon offsets (mas)
const fs=require('fs'),H=require('path').join(__dirname,'..','..','..','index.html'),s=fs.readFileSync(H,'utf8');
const grab=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);return s.slice(i,j)};
const window={};eval(fs.readFileSync(H.replace('index.html','data/sb-orbits.js'),'utf8'));
eval((s.match(/^const AU=.*$/m)[0]+'\n'+grab('const EL=','\nconst SB=')+'\n'+grab('const wrapPi=','\nconst nowJD')).replace(/(^|\n)const /g,'$1var ').replace(/(^|\n)let /g,'$1var '));
const i0=s.indexOf('const SB=');let d=0,j=i0+9;for(;j<s.length;j++){if(s[j]=='[')d++;else if(s[j]==']'){d--;if(!d)break}}
const SBl=eval(s.slice(i0+9,j+1));var byId={earth:{id:'earth',orb:'em'}};const app=require(require('path').join(__dirname,'appmoons.js'));
const PRIM={Haumea:'haumea',Eurybates:'eurybates',Hektor:'hektor',Quaoar:'quaoar',Orcus:'orcus',Patroclus:'patroclus'};
const sbo=id=>{const[,,,,a,e,i,om,w,M0,ep]=SBl.find(x=>x[0]===id);const[Pv,Qv]=PQ(om,i,w),W=window.SB_FIT[id];return{orb:'sb',a:a*AU,b:a*AU*Math.sqrt(1-e*e),e,M0,ep,n:0.9856076686/Math.pow(a,1.5),Pv,Qv,fit:W?{w:W,sb:1}:null}};
const M=JSON.parse(fs.readFileSync(process.argv[2])),out={},A=[0,0,0],E=[0,0,0],CE=Math.cos(OBL),SE=Math.sin(OBL);
const NAME={Hiiaka:'Hiʻiaka'};
for(const[sat,{primary,rows}]of Object.entries(M)){const p=sbo(PRIM[primary]),m=app(NAME[sat]||sat);out[sat]=[];
 for(const[t,dx,dy]of rows){let te=t;for(let k=0;k<3;k++){helio(p,te,A);helio(byId.earth,t,E);const D=Math.hypot(A[0]-E[0],A[1]-E[1],A[2]-E[2])/AU*149597870.7;te=t-D/299792.458/86400}
  helio(p,te,A);helio(byId.earth,t,E);let u=[A[0]-E[0],A[1]-E[1],A[2]-E[2]];const D=Math.hypot(...u)/AU*149597870.7;u=u.map(x=>x/Math.hypot(...u));
  const ue=[u[0],CE*u[1]-SE*u[2],SE*u[1]+CE*u[2]],ra=Math.atan2(ue[1],ue[0]),de=Math.asin(ue[2]);
  const toEcl=v=>[v[0],CE*v[1]+SE*v[2],-SE*v[1]+CE*v[2]];const east=toEcl([-Math.sin(ra),Math.cos(ra),0]),north=toEcl([-Math.sin(de)*Math.cos(ra),-Math.sin(de)*Math.sin(ra),Math.cos(de)]);
  const r=m.pos(te),mas=x=>x/D*206264806.247;
  out[sat].push({t,te,D,east,north,mir:[dx,dy],app:[mas(r[0]*east[0]+r[1]*east[1]+r[2]*east[2]),mas(r[0]*north[0]+r[1]*north[1]+r[2]*north[2])]})}}
fs.writeFileSync(process.argv[3],JSON.stringify(out));console.log(Object.entries(out).map(([k,v])=>k+' '+v.length).join(', '));
