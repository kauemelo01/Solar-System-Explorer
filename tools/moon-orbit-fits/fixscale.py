# Window fits match directions only, so their semi-major axis is unconstrained and drifts.
# Rescale each window's a so the model's distances match JPL Horizons' distances (median ratio) in that window.
import sys,os,json,glob
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
exec(open('fit1800.py').read().rsplit("\nif __name__=='__main__':",1)[0])
byname={j[0]:j for j in jobs}
F=np.eye(3);rep=[]
for f in sorted(glob.glob(D+'/*.json')):
    r=json.load(open(f))
    if not r or r.get('kind')!='windows' or not r.get('windows'):continue
    name=os.path.basename(f)[:-5]
    job=byname.get(name) or next((j for j in jobs if fn(j[0])==f),None)
    if job is None:rep.append((name,'no job'));continue
    _,s,ser=get(job)
    arr=np.array(ser);tt=arr[:,0]-2451545.0;H=arr[:,1:4];dH=np.linalg.norm(H,axis=1)
    for w in r['windows']:
        sel=(tt>=w['t0']-1)&(tt<=w['t1']+1)
        if sel.sum()<3:sel=np.argsort(np.abs(tt-(w['t0']+w['t1'])/2))[:6]
        m=model3(w['p'],tt[sel],F,*w['shape']);k=np.median(dH[sel]/np.linalg.norm(m,axis=1))
        w['shape'][0]=float(w['shape'][0]*k)
        d=np.linalg.norm(model3(w['p'],tt[sel],F,*w['shape']),axis=1);w['dist_err']=float(np.max(np.abs(d/dH[sel]-1)))
    json.dump(r,open(f,'w'))
    a=[w['shape'][0] for w in r['windows']];rep.append((name,min(a),max(a),max(w['dist_err'] for w in r['windows'])))
json.dump(rep,open('fixscale.json','w'))
print(len(rep),'windowed moons rescaled')
bad=[x for x in rep if len(x)<4 or x[3]>0.2];print('max distance error >20%:',len(bad),bad[:10])
for n in ['Himalia','S_2016_J_4','Carme','Nereid','S_2023_S_38']:
    x=[y for y in rep if y[0]==n];print(x)
