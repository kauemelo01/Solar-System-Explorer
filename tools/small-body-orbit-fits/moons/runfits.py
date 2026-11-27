import json,math,numpy as np,sys
from smoonfit import *
H=json.load(open('hz_dense.json'));S=json.load(open('sky_fit.json'));A=json.load(open('appinit.json'))
P={'Dysnomia':15.787167,'Weywot':11.686264,'Vanth':9.537918,'Dimorphos':0.474,'Menoetius':4.282753,'Hiiaka':49.462,'Namaka':18.2783,'Skamandrios':2.9651,'Queta':82.46}
IMPACT=2459849.4683   # DART impact, 2022-09-26 23:14 UTC
OUT={}
def win(p,t0,t1,tm):
    q=list(p)+[0]*(10-len(p));Mm,n,wm,Om,a,e,i,w1,O1,M2=q;T=tm-J2000
    return [t0-J2000,t1-J2000,Mm-n*T+.5*M2*T*T,n-M2*T,wm-w1*T,w1,Om-O1*T,O1,M2,a,e,i]
# ---- 3D: JPL Horizons
for n in ['Dysnomia','Weywot','Vanth','Dimorphos']:
    R=np.array(H[n]['rows']);a0,b0=H[n]['span'];parts=[(a0,IMPACT),(IMPACT,b0)] if n=='Dimorphos' else [(a0,b0)];W=[]
    for a,b in parts:
        m=(R[:,0]>=a)&(R[:,0]<=b);t=R[m,0];X=R[m,1:];tm=float(np.median(t))
        Ai=[r for r in A[n] if a<=r[0]<=b]
        p0=init_from(Ai,tm,P[n] if not (n=='Dimorphos' and a<IMPACT) else 0.4967)
        res=lambda q,mm:((model(q,t[mm],tm)-X[mm])/np.linalg.norm(X[mm],axis=1)[:,None]).ravel()
        p,rms=fit(t,res,p0,tm,P[n]);ang=np.linalg.norm(model(p,t,tm)-X,axis=1)/np.linalg.norm(X,axis=1)/DEG
        print(f"{n:11s} {((a-J2000)/365.25+2000):.1f}-{((b-J2000)/365.25+2000):.1f}: typical {np.sqrt(np.mean(ang**2)):.3f}°, worst {ang.max():.3f}°, P {360/p[1]*24:.4f} h, {len(p)} params",flush=True)
        W.append(win(p,a,b,tm))
    OUT[n]=dict(w=W,t=[a0,b0],src='JPL Horizons')
# ---- 2D: sky-plane offsets
for n in ['Hiiaka','Namaka','Skamandrios','Queta']:
    rows=S[n];t=np.array([r['te'] for r in rows]);E=np.array([r['east'] for r in rows]);N=np.array([r['north'] for r in rows]);D=np.array([r['D'] for r in rows]);O=np.array([r['mir'] for r in rows])
    tm=float(np.median(t))
    if n in('Hiiaka','Namaka'):   # Proudfoot et al. 2024, Table 2 (HST+Keck), J2000 ecliptic at Haumea-centric JD 2454615.0
        el={'Hiiaka':(49352,0.0545,77.376,99.05,13.071,153.88,6.65e18),'Namaka':(25548,0.2137,69.048,117.82,23.606,186.32,1.1e18)}[n]
        a,e,i,w,Om,M,ms=el;nn=math.sqrt(G*(3952.62e18+ms)/a**3)*86400/DEG
        p0=[M+nn*(tm-2454615.0),nn,w,Om,a,e,i]
    else:p0=init_from(A[n],tm,P[n])
    a0=p0[4]
    def res(q,mm):
        X=model(q,t[mm],tm);sx=np.sum(X*E[mm],1)/D[mm]*MAS;sy=np.sum(X*N[mm],1)/D[mm]*MAS;s=a0/D[mm]*MAS
        return np.concatenate([(sx-O[mm,0])/s,(sy-O[mm,1])/s])
    p,rms=fit(t,res,p0,tm,P[n]);m=np.ones(len(t),bool);r=res(p,m);k=len(t);ang=np.hypot(r[:k],r[k:])/DEG
    print(f"{n:11s} {((t.min()-J2000)/365.25+2000):.1f}-{((t.max()-J2000)/365.25+2000):.1f}: typical {np.sqrt(np.mean(ang**2)):.3f}°, worst {ang.max():.3f}°, P {360/p[1]:.5f} d, a {p[4]:.1f} km, e {p[5]:.4f}, i {p[6]:.2f}, {len(p)} params",flush=True)
    OUT[n]=dict(w=[win(p,t.min(),t.max(),tm)],t=[float(t.min()),float(t.max())],src='Proudfoot et al. 2024' if n in('Hiiaka','Namaka') else 'IMCCE Miriade (Genoide)')
json.dump(OUT,open('fits.json','w'))
