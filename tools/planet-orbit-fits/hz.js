// JPL Horizons heliocentric state vectors (J2000 ecliptic, AU and AU/day, times in UT) for the planets, cached in <SSE_WORK>/planets-hz/<id>-<tag>.json
// node hz.js [fit|check|far]   fit: the fitting samples over 1800-2050; check: test dates between them; far: 1600-1800 and 2050-2250 (extrapolation)
const fs=require('fs'),path=require('path'),os=require('os');
const WORK=process.env.SSE_WORK||path.join(os.homedir(),'solar-system-explorer-work','sbfit'),D=path.join(WORK,'planets-hz');fs.mkdirSync(D,{recursive:true});
// app id -> Horizons body (the planet itself, or the Earth-Moon barycentre) and the sample step in days (about 1/40 of the orbit, at least 50 samples per window)
const P={mercury:[199,2],venus:[299,4],emb:[3,5],mars:[499,8],jupiter:[599,20],saturn:[699,30],uranus:[799,50],neptune:[899,60],pluto:[999,60]};
async function get(code,start,stop,step){
  try{return await get1(code,start,stop,step)}catch(e){   // the span Horizons covers is shorter (Neptune from 2 Jan 1800): clip it
    const m=/(prior to|after) A\.D\. (\d{4})-(\w{3})-(\d{2})/.exec(e.message);if(!m)throw e;const y=+m[2],M={JAN:'01',FEB:'02',MAR:'03',APR:'04',MAY:'05',JUN:'06',JUL:'07',AUG:'08',SEP:'09',OCT:'10',NOV:'11',DEC:'12'}[m[3]];
    const d=`${y}-${M}-${String(+m[4]+(m[1]==='prior to'?1:-1)).padStart(2,'0')}`;if(m[1]==='prior to'){if(d>=stop)return[];start=d}else{if(d<=start)return[];stop=d}
    console.log(`  ${code}: clipped to ${start} - ${stop}`);return get1(code,start,stop,step)}}
async function get1(code,start,stop,step){
  const q={format:'text',COMMAND:`'${code}'`,EPHEM_TYPE:'VECTORS',CENTER:"'500@10'",REF_PLANE:'ECLIPTIC',REF_SYSTEM:'J2000',VEC_TABLE:"'2'",OUT_UNITS:'AU-D',
    CSV_FORMAT:'YES',TIME_TYPE:'UT',VEC_LABELS:'NO',START_TIME:`'${start}'`,STOP_TIME:`'${stop}'`,STEP_SIZE:`'${step}'`};
  let t='';
  for(let a=0;a<6;a++){try{t=await (await fetch('https://ssd.jpl.nasa.gov/api/horizons.api?'+new URLSearchParams(q))).text();if(t.includes('$$SOE'))break}catch(e){t='ERR '+e}
    await new Promise(r=>setTimeout(r,3000*(a+1)))}
  if(!t.includes('$$SOE'))throw new Error(t.slice(-400));
  return t.split('$$SOE')[1].split('$$EOE')[0].trim().split('\n').map(l=>{const c=l.split(',').map(s=>s.trim());return[+c[0],...c.slice(2,8).map(Number)]})}
async function main(){const tag=process.argv[2]||'fit';
  for(const[k,[code,step]]of Object.entries(P)){const f=path.join(D,`${k}-${tag}.json`);if(fs.existsSync(f))continue;let rows=[];
    if(tag==='fit')rows=await get(code,'1800-01-01','2051-01-01',step+' d');
    else if(tag==='check'){const h=Math.max(1,Math.round(step*3.37));rows=await get(code,'1800-01-03','2050-12-30',h+' d')}   // a step that never lands on a fitting sample
    else for(const[a,b]of[['1600-01-01','1800-01-01'],['2051-01-01','2250-01-01']])rows=rows.concat(await get(code,a,b,'73 d'));
    fs.writeFileSync(f,JSON.stringify(rows));console.log(k,tag,rows.length,'rows')}}
if(require.main===module)main().catch(e=>{console.error(e.message);process.exit(1)});
module.exports={WORK,D,P};
