import json,math,numpy as np
from smoonfit import *
S=json.load(open('sky_fit.json'));A=json.load(open('appinit.json'));OUT=json.load(open('fits.json'))
def win(p,t0,t1,tm):
    q=list(p)+[0]*(10-len(p));Mm,n,wm,Om,a,e,i,w1,O1,M2=q;T=tm-J2000
    return [t0-J2000,t1-J2000,Mm-n*T+.5*M2*T*T,n-M2*T,wm-w1*T,w1,Om-O1*T,O1,M2,a,e,i]
rows=S['Skamandrios'];t=np.array([r['te'] for r in rows]);E=np.array([r['east'] for r in rows]);N=np.array([r['north'] for r in rows]);D=np.array([r['D'] for r in rows]);Ob=np.array([r['mir'] for r in rows]);tm=float(np.median(t))
p0=init_from(A['Skamandrios'],tm,2.9651);a0=p0[4]
def res2(q,mm=None):
    mm=np.ones(len(t),bool) if mm is None else mm
    Xm=model(q,t[mm],tm);sx=np.sum(Xm*E[mm],1)/D[mm]*MAS;sy=np.sum(Xm*N[mm],1)/D[mm]*MAS;s=a0/D[mm]*MAS
    return np.concatenate([(sx-Ob[mm,0])/s,(sy-Ob[mm,1])/s])
def inplane(Om,i):
    O=Om*DEG;I=i*DEG;u=np.array([math.cos(O),math.sin(O),0]);nv=np.array([math.sin(I)*math.sin(O),-math.sin(I)*math.cos(O),math.cos(I)]);v=np.cross(nv,u)
    ang=[]
    for k in range(len(t)):
        Mx=np.array([[u@E[k],v@E[k]],[u@N[k],v@N[k]]]);xy=np.linalg.solve(Mx,Ob[k]*D[k]/MAS);ang.append(math.degrees(math.atan2(xy[1],xy[0])))
    return np.array(ang)
best=None
for Om,i,lab in ((p0[3],p0[6],'paper plane'),(p0[3]+180,180-p0[6],'reversed sense')):
    th=inplane(Om,i);n,ph,q=periodogram(t,th,121.4,0.01,tm);print(f'  {lab}: P {360/n:.6f} d, coherence {q:.3f}')
    for e0 in (0.05,0.3):
        p=[ph-p0[2],n,p0[2],Om,a0,e0,i]
        r=least_squares(lambda x:res2(x),p,bounds=(LO,HI),x_scale='jac',max_nfev=4000);c=np.sqrt(np.mean(r.fun**2))
        if best is None or c<best[0]:best=(c,r.x,lab)
c,p,lab=best
r2=least_squares(lambda x:res2(x),list(p)+[0,0,0],bounds=(LO+[-np.inf]*3,HI+[np.inf]*3),x_scale='jac',max_nfev=4000)
if np.sqrt(np.mean(r2.fun**2))<0.8*c:p=r2.x
rr=res2(p);k=len(t);ang=np.hypot(rr[:k],rr[k:])/DEG
print(f"Skamandrios ({lab}) 2001-2029: typical {np.sqrt(np.mean(ang**2)):.3f}°, worst {ang.max():.3f}°, P {360/p[1]:.6f} d, a {p[4]:.1f} km, e {p[5]:.4f}, i {p[6]:.2f}, node {p[3]%360:.2f}, {len(p)} params")
OUT['Skamandrios']['w']=[win(p,t.min(),t.max(),tm)];json.dump(OUT,open('fits.json','w'))
