import sys,os,json,time,math
sys.path.insert(0,os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work')))
exec(open(''+os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work'))+'/runfits2.py').read().split("if __name__=='__main__':")[0])
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
OUT=''+os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work'))+'/fits3.json'
def one(job):
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
if __name__=='__main__':
    t0=time.time()
    with ProcessPoolExecutor(8) as ex:res=dict(ex.map(one,jobs,chunksize=2))
    json.dump(res,open(OUT,'w'))
    import numpy as np
    g=[k for k,v in res.items() if v and v.get('kind')=='global'];w=[k for k,v in res.items() if v and v.get('kind')=='windows']
    worst=[(max(x['rms'] for x in res[k]['windows']),k) for k in w if res[k]['windows']]
    print(f"done in {time.time()-t0:.0f}s: global fits {len(g)}, windowed {len(w)}, none {[k for k,v in res.items() if not v]}, errors {[k for k,v in res.items() if v and 'error' in v][:8]}")
    allw=[x for k in w for x in res[k]['windows']]
    print('windows total',len(allw),'| window rms <=0.5:',sum(x['rms']<=0.5 for x in allw),' <=1:',sum(x['rms']<=1 for x in allw),' <=2:',sum(x['rms']<=2 for x in allw),' >5:',sum(x['rms']>5 for x in allw))
    print('worst moons (max window rms):',sorted(worst,reverse=True)[:15])
