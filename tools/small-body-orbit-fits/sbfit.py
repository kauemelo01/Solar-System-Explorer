# Fit a series of heliocentric orbits (time windows) to JPL Horizons for one small body, in the app's own orbit model.
# Usage: python sbfit.py <id>   -> <SSE_WORK>/fits/<id>.json   (python sbfit.py --list prints the ids to fit)
import sys,os,json,math,subprocess,tempfile
import numpy as np
from scipy.optimize import least_squares
from scipy.interpolate import CubicSpline
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));import hz
HERE=os.path.dirname(os.path.abspath(__file__));WORK=hz.WORK
J2000=2451545.0;DEG=math.pi/180;AUKM=149597870.7;NG=0.9856076686   # Gaussian mean motion, deg/day at 1 AU (as in the app)
TOL_A=0.25*DEG;TOL_NEAR=float(os.environ.get("SSE_TOL_NEAR","0.05"))*DEG;TOL_T=0.2;STEP=0.05;LMIN=0.02   # TOL_NEAR: seen from a planet, in its zone (flybys' timing)
PL={'venus':(0.03,0.08),'earth':(0.03,0.08),'mars':(0.03,0.08),'jupiter':(0.35,0.8)}
# ---- app planets (node) and the app's planet errors against JPL, as splines
def app_planets(T):
    with tempfile.TemporaryDirectory() as d:
        json.dump(list(map(float,T)),open(d+'/t.json','w'));subprocess.run(['node',HERE+'/appplanets.js',d+'/t.json',d+'/p.json'],check=True,env={**os.environ,'SSE_HTML':hz.REPO+'/index.html'})
        P=json.load(open(d+'/p.json'))
    return {k:np.array(v) for k,v in P.items()}
def _rows(f):
    t=open(f).read().split('$$SOE')[1].split('$$EOE')[0].strip().split('\n');return np.array([[float(c.split(',')[0])]+[float(x) for x in c.split(',')[2:5]] for c in t])
ERR={}
for p,code in (('venus',299),('earth',399),('mars',499),('jupiter',599)):
    R=_rows(hz.planet(p,code));A=app_planets(R[:,0])[p];ERR[p]=CubicSpline(R[:,0],A-R[:,1:],axis=0)
# ---- the app's orbit model (moonOrbit + ell1 for a window), vectorised
def wrapPi(x):
    x=np.fmod(x,2*math.pi);return np.where(x>math.pi,x-2*math.pi,np.where(x<-math.pi,x+2*math.pi,x))
def solveE(M,e):
    E=M+e*np.sin(M) if e<.8 else math.pi*np.where(M==0,1,np.sign(M))
    for _ in range(6 if e<.8 else 14):E=E-(E-e*np.sin(E)-M)/(1-e*np.cos(E))
    return E
def model(p,t):   # p: Mm,n,wm,Om,a,e,i[,w1,O1,M2] about tm (absolute JD in t)
    Mm,n,wm,Om,a,e,i=p[:7];w1,O1,M2=(p[7],p[8],p[9]) if len(p)>7 else (0,0,0);dt=t-TM[0]
    M=Mm+n*dt+.5*M2*dt*dt;W=(wm+w1*dt)*DEG;O=(Om+O1*dt)*DEG;I=i*DEG
    E=solveE(wrapPi(M*DEG),e);c=a*(np.cos(E)-e);s=a*math.sqrt(max(1-e*e,1e-12))*np.sin(E)
    cO,sO,cI,sI,cw,sw=np.cos(O),np.sin(O),math.cos(I),math.sin(I),np.cos(W),np.sin(W)
    P=np.array([cw*cO-sw*sO*cI,cw*sO+sw*cO*cI,sw*sI]);Q=np.array([-sw*cO-cw*sO*cI,-sw*sO+cw*cO*cI,cw*sI])
    return (P*c+Q*s).T
TM=[0]
def rv2el(r,v):
    mu=(NG*DEG)**2;rn=np.linalg.norm(r);h=np.cross(r,v);i=math.degrees(math.acos(h[2]/np.linalg.norm(h)));N=np.cross([0,0,1],h)
    ev=np.cross(v,h)/mu-r/rn;e=np.linalg.norm(ev);a=1/(2/rn-v@v/mu)
    Om=math.degrees(math.atan2(N[1],N[0]));w=math.degrees(math.atan2(np.cross(N,ev)@h/np.linalg.norm(h),N@ev))
    nu=math.atan2(np.cross(ev,r)@h/np.linalg.norm(h),ev@r);e=min(e,0.995);a=abs(a)
    E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));M=math.degrees(E-e*math.sin(E))
    return [M,NG/a**1.5,w,Om,a,e,i]
# ---- samples: Horizons states, the app's planets, fit targets and error scales
class Body:
    def __init__(s,k):
        s.k=k;s.cov=hz.coverage()[k];s.refresh()
    def refresh(s):
        S=hz.load(s.k);R=np.array([S[t] for t in sorted(S) if s.cov[0]-1e-6<=t<=s.cov[1]+1e-6]);s.t=R[:,0];s.r=R[:,1:4];s.v=R[:,4:7]
        P=app_planets(s.t);P2=app_planets(s.t+0.01);rs=np.linalg.norm(s.r,axis=1)
        s.scale=rs.copy();s.tgt=s.r.copy();s.vref=s.v.copy();s.wmax=np.zeros(len(s.t))
        for p,(R1,R2) in PL.items():
            d=np.linalg.norm(s.r-P[p],axis=1);x=np.clip((R2-d)/(R2-R1),0,1);w=x*x*(3-2*x)
            near=(d<R2)&(d<s.scale);s.scale=np.where(near,d,s.scale);vp=(P2[p]-P[p])/0.01
            s.vref=np.where(near[:,None],s.v-vp,s.vref)
            sel=w>s.wmax;s.tgt=np.where(sel[:,None],s.r+w[:,None]*ERR[p](s.t),s.tgt);s.wmax=np.maximum(s.wmax,w)
    def densify(s,rounds=8):
        for r in range(rounds):
            m=np.linalg.norm(s.vref,axis=1)/s.scale;gap=np.diff(s.t);mot=np.maximum(m[:-1],m[1:])*gap
            need=[]
            for i in np.nonzero(mot>STEP)[0]:
                n=min(int(math.ceil(mot[i]/STEP)),int(gap[i]/0.0007));need+=list(s.t[i]+gap[i]*np.arange(1,n)/n)
            if not need:return r
            print(f'  {s.k}: round {r+1}, +{len(need)} samples',flush=True);hz.tlist(s.k,[round(x,6) for x in need]);s.refresh()
        return rounds
# ---- one window
def check(B,p,m):
    res=model(p,B.t[m])-B.tgt[m];sc=B.scale[m];ang=np.linalg.norm(res,axis=1)/sc
    v=B.v[m];vn=np.linalg.norm(v,axis=1);along=np.sum(res*v,axis=1)/vn;perp=np.linalg.norm(res-along[:,None]*v/vn[:,None],axis=1)/sc
    near=sc<np.linalg.norm(B.r[m],axis=1);tol=np.where(near,TOL_NEAR,TOL_A)
    ok=(ang<=tol)|((B.wmax[m]==0)&(perp<=tol)&(np.abs(along)/vn<=TOL_T))
    return ok.all(),ang.max()
def fitwin(B,a,b):
    L=b-a;E=0.1*L;m=(B.t>=a-E)&(B.t<=b+E)
    if m.sum()<14:
        hz.tlist(B.k,[round(x,6) for x in np.linspace(max(a-E,B.cov[0]),min(b+E,B.cov[1]),30)]);B.refresh();m=(B.t>=a-E)&(B.t<=b+E)
    TM[0]=0.5*(a+b);j=np.argmin(abs(B.t[m]-TM[0]));t=B.t[m];sc=B.scale[m];tg=B.tgt[m]
    p0=rv2el(B.r[m][j],B.v[m][j]);dtj=t[j]-TM[0];p0[0]-=p0[1]*dtj
    f=lambda p:((model(p,t)-tg)/sc[:,None]).ravel()
    lo=[-np.inf,0,-np.inf,-np.inf,1e-4,0,0];hi=[np.inf,np.inf,np.inf,np.inf,np.inf,0.9995,180]
    best=None
    for npar in ((7,10) if L>400 else (7,)):
        x0=(p0 if npar==7 else list(best[0][:7])+[0,0,0])
        try:r=least_squares(f,x0,bounds=(lo+[-np.inf]*(npar-7),hi+[np.inf]*(npar-7)),x_scale='jac',max_nfev=300)
        except Exception:continue
        ok,mx=check(B,r.x,m)
        if best is None or mx<best[2]:best=(r.x,ok,mx)
        if ok:break
    return best
def run(k):
    B=Body(k);B.densify();W=[];stack=[]
    T0,T1=B.cov;n=max(1,round((T1-T0)/(20*365.25)));edges=np.linspace(T0,T1,n+1)
    stack=[(edges[i],edges[i+1]) for i in range(n)][::-1];worst=0
    while stack:
        a,b=stack.pop();p,ok,mx=fitwin(B,a,b)
        if not ok and b-a>LMIN:stack+=[((a+b)/2,b),(a,(a+b)/2)];continue
        TM[0]=0.5*(a+b);tm=TM[0]-J2000;q=list(p)+[0]*(10-len(p));Mm,n_,wm,Om,A,e,i,w1,O1,M2=q
        W.append([a-J2000,b-J2000,Mm-n_*tm+.5*M2*tm*tm,n_-M2*tm,wm-w1*tm,w1,Om-O1*tm,O1,M2,A*AUKM,e,i]);worst=max(worst,mx)
        if not ok:print(f'  {k}: window {a:.3f}-{b:.3f} left at {mx/DEG:.3f} deg',flush=True)
    os.makedirs(WORK+'/fits',exist_ok=True);json.dump(dict(w=W,n=len(B.t),worst=worst/DEG),open(f'{WORK}/fits/{k}.json','w'))
    print(f'{k}: {len(W)} windows, {len(B.t)} samples, worst {worst/DEG:.3f} deg',flush=True)
if __name__=='__main__':
    if sys.argv[1]=='--list':print('\n'.join(k for k in hz.IDS if k not in hz.SKIP))
    else:run(sys.argv[1])
