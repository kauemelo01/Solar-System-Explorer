import json,math,numpy as np
from smoonfit import *
H=json.load(open('hz_dense.json'));S=json.load(open('sky_fit.json'));OUT=json.load(open('fits.json'))
IMPACT=2459849.4683
def win(p,t0,t1,tm):
    q=list(p)+[0]*(10-len(p));Mm,n,wm,Om,a,e,i,w1,O1,M2=q;T=tm-J2000
    return [t0-J2000,t1-J2000,Mm-n*T+.5*M2*T*T,n-M2*T,wm-w1*T,w1,Om-O1*T,O1,M2,a,e,i]
def plane_angle(X,p):
    # angle of each position within the orbit plane of p, from the ascending node (deg) = mean longitude for a near-circular orbit
    O=p[3]*DEG;I=p[6]*DEG;nv=np.array([math.sin(I)*math.sin(O),-math.sin(I)*math.cos(O),math.cos(I)]);u=np.array([math.cos(O),math.sin(O),0]);v=np.cross(nv,u)
    return np.degrees(np.arctan2(X@v,X@u))
# ---- Dimorphos after the impact: periodogram on the angle within the orbit plane, then the full fit
R=np.array(H['Dimorphos']['rows']);m=R[:,0]>=IMPACT;t=R[m,0];X=R[m,1:];tm=float(np.median(t))
pre=OUT['Dimorphos']['w'][0];p=[0,0,pre[4],pre[6],pre[9],0.03,pre[11]]   # plane and size from before the impact
th=plane_angle(X,p);n,ph,q=periodogram(t,th,360/(11.38/24),0.01,tm);print(f'Dimorphos post-impact periodogram: P {360/n*24:.4f} h, coherence {q:.3f}')
p=[ph-p[2],n,p[2],p[3],p[4],0.03,p[6]]   # mean anomaly from the mean longitude (lambda = Omega + omega + M; theta from node = omega + M)
res=lambda q,mm:((model(q,t[mm],tm)-X[mm])/np.linalg.norm(X[mm],axis=1)[:,None]).ravel()
r=least_squares(lambda q:res(q,np.ones(len(t),bool)),p,bounds=(LO,HI),x_scale='jac',max_nfev=4000);p=r.x
r2=least_squares(lambda q:res(q,np.ones(len(t),bool)),list(p)+[0,0,0],bounds=(LO+[-np.inf]*3,HI+[np.inf]*3),x_scale='jac',max_nfev=4000)
if np.mean(res(r2.x,np.ones(len(t),bool))**2)<0.64*np.mean(res(p,np.ones(len(t),bool))**2):p=r2.x
ang=np.linalg.norm(model(p,t,tm)-X,axis=1)/np.linalg.norm(X,axis=1)/DEG
print(f"Dimorphos   2022.7-2027.5: typical {np.sqrt(np.mean(ang**2)):.3f}°, worst {ang.max():.3f}°, P {360/p[1]*24:.4f} h, e {p[5]:.4f}, {len(p)} params")
OUT['Dimorphos']['w'][1]=win(p,IMPACT,H['Dimorphos']['span'][1],tm)
# ---- Skamandrios: periodogram on the position angle on the sky, then the sky-plane fit
rows=S['Skamandrios'];t=np.array([r['te'] for r in rows]);E=np.array([r['east'] for r in rows]);N=np.array([r['north'] for r in rows]);D=np.array([r['D'] for r in rows]);Ob=np.array([r['mir'] for r in rows]);tm=float(np.median(t))
pa=np.degrees(np.arctan2(Ob[:,0],Ob[:,1]))
for sgn in (1,-1):
    n,ph,q=periodogram(t,sgn*pa,121.4,0.01,tm);print(f'  Skamandrios PA periodogram (sense {sgn:+d}): P {360/n:.6f} d, coherence {q:.3f}')
A=json.load(open('appinit.json'));p0=init_from(A['Skamandrios'],tm,2.9651)
best=None
for sgn in (1,-1):
    n,ph,q=periodogram(t,sgn*pa,121.4,0.01,tm)
    for dM in range(0,360,30):
        p=list(p0);p[1]=n;p[0]=p0[0]+dM;a0=p[4]
        def res2(q,mm):
            Xm=model(q,t[mm],tm);sx=np.sum(Xm*E[mm],1)/D[mm]*MAS;sy=np.sum(Xm*N[mm],1)/D[mm]*MAS;s=a0/D[mm]*MAS
            return np.concatenate([(sx-Ob[mm,0])/s,(sy-Ob[mm,1])/s])
        r=least_squares(lambda q:res2(q,np.ones(len(t),bool)),p,bounds=(LO,HI),x_scale='jac',max_nfev=3000)
        c=np.sqrt(np.mean(r.fun**2))
        if best is None or c<best[0]:best=(c,r.x,res2)
c,p,res2=best
r2=least_squares(lambda q:res2(q,np.ones(len(t),bool)),list(p)+[0,0,0],bounds=(LO+[-np.inf]*3,HI+[np.inf]*3),x_scale='jac',max_nfev=4000)
if np.sqrt(np.mean(r2.fun**2))<0.8*c:p=r2.x
rr=res2(p,np.ones(len(t),bool));k=len(t);ang=np.hypot(rr[:k],rr[k:])/DEG
print(f"Skamandrios 2001-2029: typical {np.sqrt(np.mean(ang**2)):.3f}°, worst {ang.max():.3f}°, P {360/p[1]:.6f} d, a {p[4]:.1f} km, e {p[5]:.4f}, i {p[6]:.2f}, {len(p)} params")
OUT['Skamandrios']['w']=[win(p,t.min(),t.max(),tm)]
json.dump(OUT,open('fits.json','w'))
