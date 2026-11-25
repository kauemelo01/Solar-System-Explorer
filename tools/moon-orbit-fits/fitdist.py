# Refit window fits on direction AND distance (Horizons vectors), starting from the direction-only fit (rescaled by fixscale.py).
import sys,os,json,glob,time
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
exec(open('fit1800.py').read().rsplit("\nif __name__=='__main__':",1)[0])
F=np.eye(3);WD=1.0  # 1% distance error weighs like 0.57 deg of direction
def ang(m,H):return np.degrees(np.arccos(np.clip(np.sum(m*H,1)/np.linalg.norm(m,axis=1)/np.linalg.norm(H,axis=1),-1,1)))
def refit(f):
    r=json.load(open(f));name=os.path.basename(f)[:-5]
    job=next((j for j in jobs if fn(j[0])==f),None)
    if job is None or r.get('kind')!='windows':return name,None
    _,s,ser=get(job);arr=np.array(ser);tt=arr[:,0]-2451545.0;H=arr[:,1:4];dH=np.linalg.norm(H,axis=1);out=[]
    for w in r['windows']:
        sel=(tt>=w['t0']-1)&(tt<=w['t1']+1);t=tt[sel];Hs=H[sel];d=dH[sel];Hn=Hs/d[:,None]
        p=list(w['p']);a,e,i=w['shape']
        if a<0:a=-a;p[2]+=180   # negative axis = periapsis turned by 180 deg
        q0=p+[a,e,i]
        def res(q):
            m=model3(q[:7],t,F,q[7],min(max(q[8],0),.98),q[9]);dm=np.linalg.norm(m,axis=1)
            return np.concatenate([(m/dm[:,None]-Hn).ravel(),WD*(dm/d-1)])
        try:sl=least_squares(res,q0,method='lm',max_nfev=600);q=list(sl.x)
        except Exception:q=q0
        sh=[q[7],min(max(q[8],0),.98),q[9]];m=model3(q[:7],t,F,*sh);dm=np.linalg.norm(m,axis=1)
        e1=ang(m,Hs);m0=model3(w['p'],t,F,*w['shape']);e0=ang(m0,Hs)
        nw=dict(w,p=[float(x) for x in q[:7]],shape=[float(x) for x in sh],rms=float(np.sqrt(np.mean(e1**2))),mx=float(e1.max()),dist_err=float(np.max(np.abs(dm/d-1))),dist_rms=float(np.sqrt(np.mean((dm/d-1)**2))),rms_dironly=float(np.sqrt(np.mean(e0**2))))
        out.append(nw)
    r['windows']=out;r['distfit']=True;json.dump(r,open(f,'w'))
    return name,dict(rms0=max(x['rms_dironly'] for x in out),rms=max(x['rms'] for x in out),drms=max(x['dist_rms'] for x in out),dmax=max(x['dist_err'] for x in out),n=len(out))
if __name__=='__main__':
    fs=sys.argv[1:] or [f for f in sorted(glob.glob(D+'/*.json')) if json.load(open(f)).get('kind')=='windows']
    from concurrent.futures import ProcessPoolExecutor
    t0=time.time();rep={}
    with ProcessPoolExecutor(8) as ex:
        for n,x in ex.map(refit,fs):
            rep[n]=x;print(n,x,f'{time.time()-t0:.0f}s',flush=True)
    json.dump(rep,open('fitdist.json','w'));print('done',len(rep))
