# Shared setup and fitting rule for the moon orbit fits (formerly fitall.py, runfits2.py and runfits3.py).
# Loaded by the other scripts with exec(open('fitlib.py').read()), so that a script can replace get(job),
# which downloads a moon's Horizons series for the span it fits (fit1800.py defines it for 1800-2051).
import sys,json,re,glob,os,time,math
sys.path.insert(0,os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work')))
from moonmodel import *
from appdata import load
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

# ---- the moons to fit: every moon of a planet or Pluto in index.html, with its NAIF ID from docs/catalogue/
REPO=os.environ.get('SSE_REPO',os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..')))
M,MR,SB,CORE,EL,pl=load(REPO+'/index.html')
mid=lambda n:'m-'+re.sub(r'[^a-z0-9]+','-',n.lower())
naif={}
for f in glob.glob(REPO+'/docs/catalogue/moons-*.md'):
    if 'small-bodies' in f:continue
    for l in open(f).read().split('\n'):
        m=re.search(r'<a id="([^"]+)"></a>',l)
        if m and l.startswith('|'):naif[m.group(1)]=[x.strip() for x in l.strip('|').split('|')][7]
PC={'mars':'499','jupiter':'599','saturn':'699','uranus':'799','neptune':'899','pluto':'999'}
jobs=[(x[0],naif[mid(x[0])],PC[x[1]],x[1]) for x in M if x[11] not in('dmoon','hiiaka','namaka','amoon')]   # (name, NAIF ID, planet ID, planet)

# ---- JPL mean elements (sep.html in the work folder)
T=jpltable2()

def dense(job):
    """a dense Horizons series near 2000 (12 samples per orbit, 6 orbits), so fast moons are not fitted with a wrong speed
       that matches the sparse series equally well (aliasing)"""
    name,code,prim,par=job;P=f_(T[code]['P (days)'])
    step=max(P/12,0.02);span=max(P*6,step*40)
    st=f"{step*24*60:.0f} m"
    for jd0 in (2451545.0,2458849.5,2460676.5):
        ser=hzseries(code,prim,f"JD{jd0}",f"JD{jd0+span}",st)
        if ser and len(ser)>20:return name,ser
    return name,None

def one(job):
    """fit one moon: one orbit for the whole span if it is within 0.5 deg, otherwise time windows
       (10 years, split down to 2.5; Janus and Epimetheus in 1-year windows on a 15-day series)"""
    name,code,prim,par=job
    try:
        n,s,ser=get(job)
        if s is None:return name,None
        n,dn=dense(job)
        g=fitmoon3(T,code,par,ser,dn) if dn else None
        if g and g['rms']<=0.5:return name,dict(kind='global',fit=g)
        fine=name in('Janus','Epimetheus')
        if fine:
            ser2=hzseries(code,prim,'1949-12-29','2000-01-01','15 d') or [];ser3=hzseries(code,prim,'2000-01-01','2050-01-07','15 d') or []
            ser=ser2+ser3[1:] if ser2 and ser3 else ser
        w=adaptive2(code,prim,ser,10,1.0 if fine else 10,1.0 if fine else 999)
        if g and (not w or max(x['rms'] for x in w)>=g['rms']):return name,dict(kind='global',fit=g,windows_rms=max(x['rms'] for x in w) if w else None)
        return name,dict(kind='windows',windows=w,global_rms=g['rms'] if g else None,global_fit=g)
    except Exception as e:return name,{'error':repr(e)}
