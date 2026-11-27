# Fit the planets (and the Earth-Moon barycentre, and Pluto) to JPL Horizons over 1800-2050 AD as series of heliocentric time windows,
# in the app's orbit model (the small bodies' window format). Samples: node hz.js fit (and check, far).
# Usage: python plfit.py [ids...]   -> <SSE_WORK>/planet-fits/<id>.json; prints the worst error at the fitting and the test dates
import sys,os,json,math
import numpy as np
from scipy.optimize import least_squares
WORK=os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work/sbfit'));D=WORK+'/planets-hz';OUT=WORK+'/planet-fits'
J2000=2451545.0;DEG=math.pi/180;AUKM=149597870.7;NG=0.9856076686
TOL=float(os.environ.get('SSE_PL_TOL','0.0005'))*DEG   # largest error allowed at any sample, seen from the Sun (the full 3-D error over the distance)
START=float(os.environ.get('SSE_PL_WIN','20'))*365.25  # first window length (days); windows are halved until every sample is within TOL
IDS=['mercury','venus','emb','mars','jupiter','saturn','uranus','neptune','pluto']
# ---- the app's orbit model for one window (moonOrbit + ell1 in index.html; the same as sbfit.py)
def wrapPi(x):
    x=np.fmod(x,2*math.pi);return np.where(x>math.pi,x-2*math.pi,np.where(x<-math.pi,x+2*math.pi,x))
def solveE(M,e):
    E=M+e*np.sin(M)
    for _ in range(6):E=E-(E-e*np.sin(E)-M)/(1-e*np.cos(E))
    return E
def model(p,t,tm):   # p: M, n, w, node, a (AU), e, i, w', node', M'' about time tm (JD)
    Mm,n,wm,Om,a,e,i,w1,O1,M2=p;dt=t-tm
    M=Mm+n*dt+.5*M2*dt*dt;W=(wm+w1*dt)*DEG;O=(Om+O1*dt)*DEG;I=i*DEG
    E=solveE(wrapPi(M*DEG),e);c=a*(np.cos(E)-e);s=a*math.sqrt(1-e*e)*np.sin(E)
    cO,sO,cI,sI,cw,sw=np.cos(O),np.sin(O),math.cos(I),math.sin(I),np.cos(W),np.sin(W)
    P=np.array([cw*cO-sw*sO*cI,cw*sO+sw*cO*cI,sw*sI]);Q=np.array([-sw*cO-cw*sO*cI,-sw*sO+cw*cO*cI,cw*sI])
    return (P*c+Q*s).T
def rv2el(r,v):
    mu=(NG*DEG)**2;rn=np.linalg.norm(r);h=np.cross(r,v);i=math.degrees(math.acos(h[2]/np.linalg.norm(h)));N=np.cross([0,0,1],h)
    ev=np.cross(v,h)/mu-r/rn;e=np.linalg.norm(ev);a=1/(2/rn-v@v/mu)
    Om=math.degrees(math.atan2(N[1],N[0]));w=math.degrees(math.atan2(np.cross(N,ev)@h/np.linalg.norm(h),N@ev))
    nu=math.atan2(np.cross(ev,r)@h/np.linalg.norm(h),ev@r)
    E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));M=math.degrees(E-e*math.sin(E))
    return [M,NG/a**1.5,w,Om,a,e,i,0,0,0]
def err(p,tm,t,r):return np.linalg.norm(model(p,t,tm)-r,axis=1)/np.linalg.norm(r,axis=1)
# ---- one window, fitted over its span plus 10% each side (where the app blends it with its neighbours)
def fitwin(t,r,v,a,b):
    E=0.1*(b-a);m=(t>=a-E)&(t<=b+E);tm=0.5*(a+b);T,R=t[m],r[m];j=np.argmin(abs(T-tm))
    p0=rv2el(R[j],v[m][j]);p0[0]-=p0[1]*(T[j]-tm);sc=np.linalg.norm(R,axis=1)[:,None]
    lo=[-np.inf,0,-np.inf,-np.inf,1e-3,0,0]+[-np.inf]*3;hi=[np.inf]*5+[0.99,180]+[np.inf]*3
    x=least_squares(lambda p:((model(p,T,tm)-R)/sc).ravel(),p0,bounds=(lo,hi),x_scale='jac',xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=400).x
    return x,tm,err(x,tm,T,R).max()
def run(k):
    R=np.array(json.load(open(f'{D}/{k}-fit.json')));t,r,v=R[:,0],R[:,1:4],R[:,4:7]
    T0,T1=t[0],t[-1];n=max(1,round((T1-T0)/START));e=np.linspace(T0,T1,n+1);stack=[(e[i],e[i+1]) for i in range(n)][::-1];W=[];worst=0
    while stack:
        a,b=stack.pop();p,tm,mx=fitwin(t,r,v,a,b)
        if mx>TOL and b-a>200:stack+=[((a+b)/2,b),(a,(a+b)/2)];continue
        worst=max(worst,mx);Mm,n_,wm,Om,A,ec,i,w1,O1,M2=p;s=tm-J2000   # to the window format, about J2000: [t0,t1,M0,n,w0,w',node0,node',M'',a km,e,i]
        W.append([a-J2000,b-J2000,Mm-n_*s+.5*M2*s*s,n_-M2*s,wm-w1*s,w1,Om-O1*s,O1,M2,A*AUKM,ec,i])
    os.makedirs(OUT,exist_ok=True);json.dump(dict(w=W,worst=worst/DEG),open(f'{OUT}/{k}.json','w'))
    print(f'{k}: {len(W)} windows (shortest {min(w[1]-w[0] for w in W)/365.25:.1f} yr), worst {worst/DEG*3600:.2f}" at the fitting samples',flush=True)
if __name__=='__main__':
    for k in sys.argv[1:] or IDS:run(k)
