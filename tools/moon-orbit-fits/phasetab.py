# For moons whose single-orbit fit stays poor (resonant swaps and librations, short-arc orbits): keep a dense single-orbit
# fit and add a table of along-track corrections every K days, measured directly from Horizons positions. Writes 'c' into the fit file.
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
exec(open('fit1800.py').read().rsplit("\nif __name__=='__main__':",1)[0])
import numpy as np
JOB={j[0]:j for j in jobs}
K={'Janus':5,'Epimetheus':5,'Helene':10,'Polydeuces':10,'S/2009 S 2':10,'S/2025 U 1':5}
def chunks(code,prim,a,b,step_d,per=3000):
    """Horizons positions on an even grid of step_d days from a to b, fetched in pieces of `per` points"""
    from datetime import date
    jd=lambda x:date.fromisoformat(x).toordinal()-date(2000,1,1).toordinal()+2451544.5
    j0,j1=jd(a),jd(b);out=[];k=0
    while j0+k*step_d<=j1:
        s0=j0+k*step_d;s1=min(j1,s0+(per-1)*step_d)
        p=hzseries(code,prim,f'JD{s0:.1f}',f'JD{s1:.1f}',f'{step_d} d') or []
        out+=p[1:] if out and p and abs(p[0][0]-out[-1][0])<1e-6 else p
        k+=per-1
        if s1>=j1:break
    return out
def one_c(name):
    job=JOB[name];_,code,prim,par=job;a,b=span(name)
    n,s,ser=get(job);n,dn=dense(job);g=fitmoon3(T,code,par,ser+dn,dn)
    knots=np.array(chunks(code,prim,a,b,K[name]))
    assert np.allclose(np.diff(knots[:,0]),K[name]),'uneven knots';t=knots[:,0]-2451545.0;H=knots[:,1:4]
    F=frame(g['ra'],g['dec']);p=g['p'];sh=g['shape']
    m=model3(p,t,F,*sh);m2=model3(p,t+0.01,F,*sh);N=np.cross(m,m2);N/=np.linalg.norm(N,axis=1)[:,None]
    r=np.degrees(np.unwrap(np.arctan2(np.sum(N*np.cross(m,H),1),np.sum(m*H,1))))
    if np.any(np.abs(np.diff(r))>90):print(name,'WARNING: large jump between knots',float(np.abs(np.diff(r)).max()))
    # check on the knots themselves after correction
    def corr(tq):return np.interp(tq,t,r)
    pc=list(p);m3=model3(pc,t,F,*sh)
    res=dict(kind='global',fit=g,span=(a,b),c=[float(t[0]),float(K[name])]+[round(float(x),3) for x in r],note=f'dense single orbit plus along-track corrections every {K[name]} days')
    json.dump(res,open(fn(name),'w'));return name,len(r),float(np.abs(r).max())
if __name__=='__main__':
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(6) as ex:
        for x in ex.map(one_c,list(K)):print(x,flush=True)
