# Single-orbit fits with a fitted shape: rescale a so model distances match JPL Horizons (directions are scale-free)
import sys,os,json,glob
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
exec(open('fit1800.py').read().rsplit("\nif __name__=='__main__':",1)[0])
F=np.eye(3)
for f in sorted(glob.glob(D+'/*.json')):
    r=json.load(open(f))
    if not r or r.get('kind')!='global' or not r['fit'].get('shapefit'):continue
    job=next((j for j in jobs if fn(j[0])==f),None);_,s,ser=get(job)
    arr=np.array(ser);tt=arr[:,0]-2451545.0;dH=np.linalg.norm(arr[:,1:4],axis=1);g=r['fit']
    sh=list(g['shape']);neg=sh[0]<0;sh[0]=abs(sh[0])
    dm=np.linalg.norm(model3(g['p'][:7],tt,F,*sh),axis=1);k=np.median(dH/dm);sh[0]*=k
    dm=np.linalg.norm(model3(g['p'][:7],tt,F,*sh),axis=1)
    if neg:g['p'][2]+=180
    print(os.path.basename(f),f"a {g['shape'][0]:.4g} -> {sh[0]:.6g} km, distance error rms {np.sqrt(np.mean((dm/dH-1)**2)):.3f} max {np.max(np.abs(dm/dH-1)):.3f}")
    g['shape']=sh;json.dump(r,open(f,'w'))
