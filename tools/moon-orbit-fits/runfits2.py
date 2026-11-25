import sys,os,json,time,math
sys.path.insert(0,os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work')))
exec(open(''+os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work'))+'/fitall.py').read().split('t0=time.time()')[0])
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
T=jpltable2()
def dense(job):
    name,code,prim,par=job;P=f_(T[code]['P (days)'])
    step=max(P/12,0.02);span=max(P*6,step*40)
    st=f"{step*24*60:.0f} m";stop=2451545.0+span
    for jd0 in (2451545.0,2458849.5,2460676.5):
        ser=hzseries(code,prim,f"JD{jd0}",f"JD{jd0+span}",st)
        if ser and len(ser)>20:return name,ser
    return name,None
def one(job):
    name,code,prim,par=job
    n,s,ser=get(job)
    if s is None:return name,None
    dn=DENSE.get(name)
    if not dn:return name,{'error':'no dense series'}
    try:r=fitmoon3(T,code,par,ser,dn)
    except Exception as e:return name,{'error':repr(e)}
    r['span_req']=s;return name,r
if __name__=='__main__':
    t0=time.time()
    with ThreadPoolExecutor(5) as ex:DENSE=dict(ex.map(dense,jobs))
    print('dense series:',sum(1 for v in DENSE.values() if v),'missing',[k for k,v in DENSE.items() if not v],round(time.time()-t0),'s')
    json.dump(DENSE,open(''+os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work'))+'/dense.json','w'))
    t0=time.time()
    with ProcessPoolExecutor(12) as ex:res=dict(ex.map(one,jobs,chunksize=3))
    json.dump(res,open(''+os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work'))+'/fits2.json','w'))
    ok=[(k,v) for k,v in res.items() if v and 'rms' in v];import numpy as np;r=np.array([v['rms'] for k,v in ok])
    print(f'fitted {len(ok)}/{len(res)} in {time.time()-t0:.0f}s; errors: {[(k,v) for k,v in res.items() if v and "error" in v][:5]}')
    for th in (0.5,1,2,5,10,20):print(f'  rms <= {th:>4} deg: {int((r<=th).sum())}')
    print('worst 20:',sorted(((round(v["rms"],1),k) for k,v in ok),reverse=True)[:20])
