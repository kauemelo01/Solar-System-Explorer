# Run from a work folder (for example $SSE_WORK/moons): files are read and written in the current folder.
# Fit the moons of dwarf planets and asteroids to a reference ephemeris, in the app's moon-window orbit model (J2000 ecliptic).
# 3D: JPL Horizons positions relative to the primary; 2D: sky-plane offsets (Proudfoot et al. 2024; IMCCE Miriade), with light time.
import json,math,numpy as np
from scipy.optimize import least_squares
DEG=math.pi/180;J2000=2451545.0;G=6.6743e-20;MAS=206264806.247
def wrapPi(x):
    x=np.fmod(x,2*math.pi);return np.where(x>math.pi,x-2*math.pi,np.where(x<-math.pi,x+2*math.pi,x))
def solveE(M,e):
    E=M+e*np.sin(M) if e<.8 else math.pi*np.where(M==0,1,np.sign(M))
    for _ in range(6 if e<.8 else 14):E=E-(E-e*np.sin(E)-M)/(1-e*np.cos(E))
    return E
def model(p,t,tm):
    Mm,n,wm,Om,a,e,i=p[:7];w1,O1,M2=(p[7],p[8],p[9]) if len(p)>7 else (0,0,0);dt=t-tm
    M=Mm+n*dt+.5*M2*dt*dt;W=(wm+w1*dt)*DEG;O=(Om+O1*dt)*DEG;I=i*DEG
    E=solveE(wrapPi(M*DEG),e);c=a*(np.cos(E)-e);s=a*math.sqrt(max(1-e*e,1e-12))*np.sin(E)
    cO,sO,cI,sI,cw,sw=np.cos(O),np.sin(O),math.cos(I),math.sin(I),np.cos(W),np.sin(W)
    P=np.array([cw*cO-sw*sO*cI,cw*sO+sw*cO*cI,sw*sI]);Q=np.array([-sw*cO-cw*sO*cI,-sw*sO+cw*cO*cI,cw*sI])
    return (P*c+Q*s).T
def rv2el(r,v,mu):
    rn=np.linalg.norm(r);h=np.cross(r,v);i=math.degrees(math.acos(h[2]/np.linalg.norm(h)));N=np.cross([0,0,1],h)
    ev=np.cross(v,h)/mu-r/rn;e=min(np.linalg.norm(ev),0.95);a=1/(2/rn-v@v/mu)
    Om=math.degrees(math.atan2(N[1],N[0]));w=math.degrees(math.atan2(np.cross(N,ev)@h/np.linalg.norm(h),N@ev))
    nu=math.atan2(np.cross(ev,r)@h/np.linalg.norm(h),ev@r);E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
    return [math.degrees(E-e*math.sin(E)),0,w,Om,a,e,i]
LO=[-np.inf,0,-np.inf,-np.inf,0.01,0,0];HI=[np.inf,np.inf,np.inf,np.inf,np.inf,0.95,180]
def fit(t,resid,p0,tm,P):
    # widen the span step by step from the centre, so the mean motion is never aliased by a whole number of turns
    order=np.argsort(abs(t-tm));p=np.array(p0,float);n=min(len(t),60)
    while True:
        m=np.zeros(len(t),bool);m[order[:n]]=True
        r=least_squares(lambda q:resid(q,m),p,bounds=(LO,HI),x_scale='jac',max_nfev=2000);p=r.x
        if n>=len(t):break
        n=min(len(t),n*2)
    m=np.ones(len(t),bool);best=(p,np.sqrt(np.mean(resid(p,m)**2)))
    r=least_squares(lambda q:resid(q,m),list(p)+[0,0,0],bounds=(LO+[-np.inf]*3,HI+[np.inf]*3),x_scale='jac',max_nfev=4000)
    rms=np.sqrt(np.mean(resid(r.x,m)**2))
    if rms<0.8*best[1]:best=(r.x,rms)
    return best
def init_from(appxyz,tm,P):
    # the app's current orbit, as starting elements about tm (fit to its own positions)
    t=np.array([r[0] for r in appxyz]);X=np.array([r[1:] for r in appxyz]);j=np.argmin(abs(t-tm))
    dt=np.median(np.diff(np.sort(t)));k=min(len(t)-1,j+1)
    v=(X[k]-X[j-1 if j>0 else j])/(t[k]-t[j-1 if j>0 else j]);mu=(2*math.pi/P)**2*np.linalg.norm(X[j])**3
    p=rv2el(X[j],v,mu);p[1]=360/P;TM=t[j]
    res=lambda q,m:((model(q,t[m],TM)-X[m])/np.linalg.norm(X[m],axis=1)[:,None]).ravel()
    p,_=fit(t,res,p,TM,P);p=list(p[:7]);p[0]+=p[1]*(tm-TM);return p
def periodogram(t,theta,n0,rel=0.01,tm=0):
    """mean motion (deg/day) whose phase best lines up across all dates: max |sum exp(i(theta - n dt))|"""
    T=t.max()-t.min();step=0.05*360/T;N=np.arange(n0*(1-rel),n0*(1+rel),step);th=np.radians(theta);dt=t-tm
    P=np.array([abs(np.exp(1j*(th-np.radians(n*dt))).sum()) for n in N]);k=int(P.argmax())
    lo,hi=N[max(k-1,0)],N[min(k+1,len(N)-1)]
    for _ in range(40):                      # refine around the peak
        F=np.linspace(lo,hi,21);Q=[abs(np.exp(1j*(th-np.radians(f*dt))).sum()) for f in F];j=int(np.argmax(Q));lo,hi=F[max(j-1,0)],F[min(j+1,20)]
    n=F[j];ph=np.degrees(np.angle(np.exp(1j*(th-np.radians(n*dt))).sum()));return n,ph,P[k]/len(t)
