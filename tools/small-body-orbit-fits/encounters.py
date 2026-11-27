# Close encounters 1800-2050 (targets: within 0.05 AU of Venus, Earth, the Moon or Mars; inside Jupiter's Hill sphere, 0.35 AU),
# found in each body's Horizons samples, then refined with planet-centred Horizons vectors. -> encounters.json
import sys,os,json,math,urllib.request,urllib.parse,time
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));import hz
from sbfit import app_planets,ERR
LIM={'venus':0.05,'earth':0.05,'mars':0.05,'jupiter':0.35}
CEN={'venus':'299','earth':'399','mars':'499','jupiter':'599','moon':'301'}
def hzrel(k,c,a,b,step):
    q=dict(format='text',COMMAND=hz.cmd(k),EPHEM_TYPE='VECTORS',CENTER=f"'500@{c}'",REF_PLANE='ECLIPTIC',REF_SYSTEM='J2000',VEC_TABLE="'1'",OUT_UNITS='KM-S',CSV_FORMAT='YES',TIME_TYPE='UT',
           START_TIME=f"'JD{a:.6f}'",STOP_TIME=f"'JD{b:.6f}'",STEP_SIZE=f"'{step}'")
    for i in range(8):
        t=''
        try:
            t=urllib.request.urlopen('https://ssd.jpl.nasa.gov/api/horizons.api?'+urllib.parse.urlencode(q),timeout=300).read().decode()
            if '$$SOE' in t:break
        except Exception:pass
        time.sleep(10+10*i)
    if '$$SOE' not in t:raise RuntimeError(t[-300:])
    R=np.array([[float(c.split(',')[0])]+[float(x) for x in c.split(',')[2:5]] for c in t.split('$$SOE')[1].split('$$EOE')[0].strip().split('\n')])
    d=np.linalg.norm(R[:,1:],axis=1);i=int(d.argmin());return R[i,0],d[i]
def refine(k,c,t0,span):
    # two passes of 400 equal steps: +-span, then +-2 steps around the closest one (resolution span/40000)
    t,d=hzrel(k,c,t0-span,t0+span,'400');s2=span/100;return hzrel(k,c,t-s2,t+s2,'400')
PART=os.path.join(hz.WORK if hasattr(hz,'WORK') else '.','encounters_partial.json')
DONE=json.load(open(PART)) if os.path.exists(PART) else {}
out=[e for v in DONE.values() for e in v]
for k in [k for k in hz.IDS if k not in hz.SKIP]:
    if k in DONE:continue
    n0=len(out)
    S=hz.load(k);R=np.array([S[t] for t in sorted(S)]);t=R[:,0];r=R[:,1:4];P=app_planets(t)
    for p,lim in LIM.items():
        jp=P[p]-ERR[p](t);d=np.linalg.norm(r-jp,axis=1)
        for i in range(1,len(d)-1):
            if d[i]<=d[i-1] and d[i]<=d[i+1] and d[i]<lim*1.3:
                span=max(1.0,(t[i+1]-t[i-1]));tt,dd=refine(k,CEN[p],t[i],span)
                if dd/149597870.7<lim:out.append(dict(id=k,body=p,jd=tt,km=dd));print(k,p,round(tt,4),round(dd),flush=True)
                if p=='earth':
                    tm,dm=refine(k,'301',t[i],6.0)   # the Moon's closest point can be days from the Earth's: search +-6 days
                    if dm/149597870.7<0.05:out.append(dict(id=k,body='moon',jd=tm,km=dm));print(k,'moon',round(tm,4),round(dm),flush=True)
    DONE[k]=out[n0:];json.dump(DONE,open(PART,'w'))
json.dump(out,open(hz.WORK+'/encounters.json','w'));print(len(out),'encounters')
