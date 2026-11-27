// JPL Horizons heliocentric positions (J2000 ecliptic, AU, times in UT) of the planets, the Earth-Moon barycentre and Pluto, to measure the app's planets against.
// Cached in <SSE_WORK>/planets-hz/<id>-<tag>.json (SSE_WORK defaults to ~/solar-system-explorer-work/sbfit).
// node hz.js [check|far|wide]
//   check: 1800-2050, every ~3.4 sample steps (7 days for Mercury to 202 days for Neptune and Pluto), the planets themselves (Neptune and Pluto from 2 Jan 1800, where Horizons starts them)
//   far:   1600-1800 and 2051-2250 every 73 days, the planets themselves
//   wide:  1000-1600 and 2250-3000 every 365 days, and for Neptune and Pluto also 1600-1800 every 73 days: the system barycentres, which Horizons covers over the whole span
//          (Standish and Williams's elements are for the barycentres; the difference from the planets' centres is far below a second of arc)
const fs=require('fs'),path=require('path'),os=require('os');
const WORK=process.env.SSE_WORK||path.join(os.homedir(),'solar-system-explorer-work','sbfit'),D=path.join(WORK,'planets-hz');fs.mkdirSync(D,{recursive:true});
// app id -> Horizons planet, Horizons barycentre, check step (days)
const P={mercury:[199,1,7],venus:[299,2,13],emb:[3,3,17],mars:[499,4,27],jupiter:[599,5,67],saturn:[699,6,101],uranus:[799,7,168],neptune:[899,8,202],pluto:[999,9,202]};
async function get(code,start,stop,step){
  try{return await get1(code,start,stop,step)}catch(e){   // the span Horizons covers is shorter (Neptune and Pluto from 2 Jan 1800): clip it
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
async function main(){const tag=process.argv[2]||'check';
  for(const[k,[code,bary,step]]of Object.entries(P)){const f=path.join(D,`${k}-${tag}.json`);if(fs.existsSync(f))continue;let rows=[];
    if(tag==='check')rows=await get(code,'1800-01-03','2050-12-30',step+' d');
    else if(tag==='far')for(const[a,b]of[['1600-01-01','1800-01-01'],['2051-01-01','2250-01-01']])rows=rows.concat(await get(code,a,b,'73 d'));
    else{for(const[a,b]of[['1000-01-01','1600-01-01'],['2250-01-01','3000-01-01']])rows=rows.concat(await get1(bary,a,b,'365 d'));
      if(k==='neptune'||k==='pluto')rows=rows.concat(await get1(bary,'1600-01-01','1800-01-01','73 d'))}
    fs.writeFileSync(f,JSON.stringify(rows));console.log(k,tag,rows.length,'rows')}}
if(require.main===module)main().catch(e=>{console.error(e.message);process.exit(1)});
module.exports={WORK,D,P};
