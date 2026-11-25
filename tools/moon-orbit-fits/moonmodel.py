import math,re,html,json,urllib.request,urllib.parse,os,glob
S=os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work'))
D=math.pi/180;OB=23.4392911*D
def eq2ecl(x,y,z):return [x, math.cos(OB)*y+math.sin(OB)*z, -math.sin(OB)*y+math.cos(OB)*z]
def PQ(node,inc,w,ra,dec):
    O,I,W=node*D,inc*D,w*D;cO,sO,cI,sI,cw,sw=math.cos(O),math.sin(O),math.cos(I),math.sin(I),math.cos(W),math.sin(W)
    P=[cw*cO-sw*sO*cI,cw*sO+sw*cO*cI,sw*sI];Q=[-sw*cO-cw*sO*cI,-sw*sO+cw*cO*cI,cw*sI]
    if ra is None:return P,Q
    a,d=ra*D,dec*D;X=[-math.sin(a),math.cos(a),0];Z=[math.cos(d)*math.cos(a),math.cos(d)*math.sin(a),math.sin(d)]
    Y=[Z[1]*X[2]-Z[2]*X[1],Z[2]*X[0]-Z[0]*X[2],Z[0]*X[1]-Z[1]*X[0]]
    tr=lambda v:eq2ecl(*[X[k]*v[0]+Y[k]*v[1]+Z[k]*v[2] for k in range(3)]);return tr(P),tr(Q)
def solveE(M,e):
    E=M+e*math.sin(M) if e<.8 else math.pi*(1 if M>=0 else -1)
    for _ in range(30):E-=(E-e*math.sin(E)-M)/(1-e*math.cos(E))
    return E
def pos(el,jd):
    a,e,w,M0,i,node,P,ra,dec,ep,wd,nd=[el[k] for k in('a','e','w','M','i','node','P','ra','dec','ep','wdot','ndot')]
    dt=jd-ep;w2=w+wd*dt;n2=node+nd*dt;M=(M0+360/P*dt+el.get('mcorr',0)*dt)
    Pv,Qv=PQ(n2,i,w2,ra,dec);Mr=((M+180)%360-180)*D;E=solveE(Mr,e);c=a*(math.cos(E)-e);s=a*math.sqrt(1-e*e)*math.sin(E)
    return [Pv[k]*c+Qv[k]*s for k in range(3)]
_hc={}
def hzvec(code,prim,jd):
    key=(code,prim,jd)
    f=f'{S}/hzcache/{code}_{prim}_{jd}.json'
    if os.path.exists(f):return json.load(open(f))
    q=dict(format='json',COMMAND=f"'{code}'",EPHEM_TYPE='VECTORS',CENTER=f"'@{prim}'",START_TIME=f"'JD{jd}'",STOP_TIME=f"'JD{jd+1}'",STEP_SIZE="'1 d'",REF_PLANE="'ECLIPTIC'",OUT_UNITS="'KM-D'",VEC_TABLE="'1'",CSV_FORMAT="'YES'")
    r=json.load(urllib.request.urlopen('https://ssd.jpl.nasa.gov/api/horizons.api?'+urllib.parse.urlencode(q),timeout=120))['result']
    m=re.search(r'\$\$SOE\s*(.*?)\s*\$\$EOE',r,flags=re.S)
    v=[float(x) for x in m.group(1).split('\n')[0].split(',')[2:5]] if m else None
    os.makedirs(f'{S}/hzcache',exist_ok=True);json.dump(v,open(f,'w'));return v
def ang(a,b):
    c=sum(x*y for x,y in zip(a,b))/math.hypot(*a)/math.hypot(*b);return math.degrees(math.acos(max(-1,min(1,c))))
def jpltable():
    s=open(S+'/sep.html',encoding='utf-8',errors='ignore').read()
    txt=lambda x:re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',x))).strip()
    ep_at=[(m.start(),m.group(1)) for m in re.finditer(r'Epoch:\s*(?:<[^>]+>\s*)*([0-9-]+(?:\.5)?)',s)]
    T={}
    for m in re.finditer(r'<table.*?</table>',s,flags=re.S):
        t=m.group(0);hdr=[txt(c) for c in re.findall(r'<th[^>]*>(.*?)</th>',t,flags=re.S)]
        ep=max((e for e in ep_at if e[0]<m.start()),default=(0,'?'))[1]
        for r in re.findall(r'<tr[^>]*>(.*?)</tr>',t,flags=re.S):
            c=[txt(x) for x in re.findall(r'<td[^>]*>(.*?)</td>',r,flags=re.S)]
            if len(c)>=11 and re.fullmatch(r'\d+',c[1]):
                d=dict(zip(hdr,c));d['epoch']=ep;T[c[1]]=d
    return T
def epjd(s):
    y,mo,dd=s.split('-');from datetime import date
    frac=0.5 if dd.endswith('.5') else 0.0
    return (date(int(y),int(mo),int(float(dd))).toordinal()-date(2000,1,1).toordinal())+2451544.5+frac
POLES={'uranus':(77.311,15.175),'neptune':(299.36,43.46),'pluto':(132.993,-6.163)}
f_=lambda x:float(x.rstrip('.')) if x not in('','-','n/a',None) else None
def elem(T,code,parent,hyp='anom',pole=None):
    r=T[code];pa=f_(r.get('P apsis (yr)'));pn=f_(r.get('P node (yr)'))
    wd=360/(pa*365.25) if pa else 0;nd=-360/(pn*365.25) if pn else 0
    ra,dec=f_(r.get('R.A. (deg)')),f_(r.get('Dec. (deg)'))
    if ra is None and parent in POLES:ra,dec=pole or POLES[parent]
    e=dict(a=f_(r['a (km)']),e=f_(r['e']),w=f_(r['ω (deg)']),M=f_(r['M (deg)']),i=f_(r['i (deg)']),node=f_(r['node (deg)']),P=f_(r['P (days)']),
           ra=ra,dec=dec,ep=epjd(r['epoch']),wdot=wd,ndot=nd)
    if hyp=='none':e['wdot']=e['ndot']=0
    if hyp=='sidereal':e['mcorr']=-wd-nd
    return e
def hzseries(code,prim,start,stop,step):
    f=f'{S}/hzcache/series_{code}_{prim}_{start}_{stop}_{step}.json'
    if os.path.exists(f):return json.load(open(f))
    q=dict(format='json',COMMAND=f"'{code}'",EPHEM_TYPE='VECTORS',CENTER=f"'@{prim}'",START_TIME=f"'{start}'",STOP_TIME=f"'{stop}'",STEP_SIZE=f"'{step}'",REF_PLANE="'ECLIPTIC'",OUT_UNITS="'KM-D'",VEC_TABLE="'1'",CSV_FORMAT="'YES'",TIME_TYPE="'TDB'")
    import time as _t
    r=None
    for k in range(5):
        try:r=json.load(urllib.request.urlopen('https://ssd.jpl.nasa.gov/api/horizons.api?'+urllib.parse.urlencode(q),timeout=300))['result']
        except Exception as e:r=None
        if r and '$$SOE' in r:break
        if r and 'No ephemeris' in r:break
        _t.sleep(5*(k+1))
    if not r:return None
    m=re.search(r'\$\$SOE\s*(.*?)\s*\$\$EOE',r,flags=re.S)
    if not m:return None
    out=[]
    for l in m.group(1).strip().split('\n'):
        c=l.split(',');out.append([float(c[0])]+[float(x) for x in c[2:5]])
    os.makedirs(f'{S}/hzcache',exist_ok=True);json.dump(out,open(f,'w'));return out
def pos2(el,jd,dM=0.0,dn=0.0,acc=0.0):
    dt=jd-2451545.0;dte=jd-el['ep']
    w=el['w']+el['wdot']*dte;node=el['node']+el['ndot']*dte
    M=el['M']+(360/el['P']+el.get('mcorr',0))*dte+dM+dn*dt+0.5*acc*dt*dt
    Pv,Qv=PQ(node,el['i'],w,el['ra'],el['dec']);E=solveE(((M+180)%360-180)*D,el['e'])
    c=el['a']*(math.cos(E)-el['e']);s=el['a']*math.sqrt(1-el['e']**2)*math.sin(E)
    return [Pv[k]*c+Qv[k]*s for k in range(3)],Pv,Qv
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def fit(base,series,quad=False):
    """fit along-track phase (dM, dn[, acc]) to Horizons positions; returns params, rms and max 3D angle error"""
    import statistics
    ts=[];res=[]
    prev=None
    for jd,x,y,z in series:
        m,Pv,Qv=pos2(base,jd);N=cross(Pv,Qv);h=[x,y,z]
        r=math.degrees(math.atan2(sum(a*b for a,b in zip(N,cross(m,h))),sum(a*b for a,b in zip(m,h))))
        if prev is not None:
            while r-prev>180:r-=360
            while r-prev<-180:r+=360
        prev=r;ts.append(jd-2451545.0);res.append(r)
    n=len(ts)
    # least squares: res = c0 + c1 t (+ c2 t^2/2)
    import numpy as np
    A=np.array([[1,t]+([0.5*t*t] if quad else []) for t in ts]);b=np.array(res)
    c=np.linalg.lstsq(A,b,rcond=None)[0]
    dM,dn=c[0],c[1];acc=c[2] if quad else 0.0
    errs=[ang(pos2(base,jd,dM,dn,acc)[0],[x,y,z]) for jd,x,y,z in series]
    return dict(dM=float(dM),dn=float(dn),acc=float(acc),rms=float(np.sqrt(np.mean(np.square(errs)))),mx=float(max(errs)))
def variants(T,code,parent):
    out=[]
    for pm in ('anom','sidereal'):
        for ws in (1,-1):
            for ns in (1,-1):
                e=elem(T,code,parent,pm);e['wdot']*=ws;e['ndot']*=ns;e['v']=(pm,ws,ns);out.append(e)
    e=elem(T,code,parent,'none');e['v']=('none',0,0);out.append(e)
    return out
import numpy as np
def epjd2(s):
    m=re.match(r'(\d+)-(\d+)-(\d+)(\.\d+)?',s);from datetime import date
    y,mo,d=int(m.group(1)),int(m.group(2)),int(m.group(3));fr=float(m.group(4) or 0)
    return (date(y,mo,d).toordinal()-date(2000,1,1).toordinal())+2451544.5+fr
def jpltable2():
    s=open(S+'/sep.html',encoding='utf-8',errors='ignore').read()
    txt=lambda x:re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',x))).strip()
    ep_at=[(m.start(),m.group(1)) for m in re.finditer(r'Epoch:\s*(?:<[^>]+>\s*)*([0-9]+-[0-9]+-[0-9]+(?:\.[0-9]+)?)',s)]
    T={}
    for m in re.finditer(r'<table.*?</table>',s,flags=re.S):
        t=m.group(0);hdr=[txt(c) for c in re.findall(r'<th[^>]*>(.*?)</th>',t,flags=re.S)]
        ep=max((e for e in ep_at if e[0]<m.start()),default=(0,'?'))[1]
        for r in re.findall(r'<tr[^>]*>(.*?)</tr>',t,flags=re.S):
            c=[txt(x) for x in re.findall(r'<td[^>]*>(.*?)</td>',r,flags=re.S)]
            if len(c)>=11 and re.fullmatch(r'\d+',c[1]):d=dict(zip(hdr,c));d['epoch']=ep;d['ep']=epjd2(ep);T[c[1]]=d
    return T
def frame(ra,dec):
    """3x3 matrix taking plane-frame vectors to ecliptic J2000 (None = ecliptic)"""
    if ra is None:return np.eye(3)
    a,d=ra*D,dec*D;X=np.array([-math.sin(a),math.cos(a),0]);Z=np.array([math.cos(d)*math.cos(a),math.cos(d)*math.sin(a),math.sin(d)]);Y=np.cross(Z,X)
    E=np.array([[1,0,0],[0,math.cos(OB),math.sin(OB)],[0,-math.sin(OB),math.cos(OB)]])
    return E@np.column_stack([X,Y,Z])
def kepler_vec(M,e):
    E=M+e*np.sin(M) if e<.8 else np.pi*np.sign(M+1e-12)
    for _ in range(40):E=E-(E-e*np.sin(E)-M)/(1-e*np.cos(E))
    return E
def model(p,t,a,e,inc,F):
    """p=[M0,n,w0,wd,O0,od,acc,A,f,ph]; t=days from J2000; returns Nx3 ecliptic vectors"""
    M0,n,w0,wd,O0,od,acc,A,fq,ph=p
    M=np.radians(M0+n*t+0.5*acc*t*t+A*np.sin(fq*t+ph));w=np.radians(w0+wd*t);O=np.radians(O0+od*t);I=math.radians(inc)
    Mw=(M+np.pi)%(2*np.pi)-np.pi;E=kepler_vec(Mw,e)
    x=a*(np.cos(E)-e);y=a*math.sqrt(1-e*e)*np.sin(E)
    cO,sO,cw,sw,cI,sI=np.cos(O),np.sin(O),np.cos(w),np.sin(w),math.cos(I),math.sin(I)
    P=np.stack([cw*cO-sw*sO*cI,cw*sO+sw*cO*cI,sw*sI],1);Q=np.stack([-sw*cO-cw*sO*cI,-sw*sO+cw*cO*cI,cw*sI],1)
    v=P*x[:,None]+Q*y[:,None];return v@F.T
from scipy.optimize import least_squares
def angerr(p,t,a,e,inc,F,H):
    m=model(p,t,a,e,inc,F);c=np.sum(m*H,1)/np.linalg.norm(m,axis=1)/np.linalg.norm(H,axis=1)
    return np.degrees(np.arccos(np.clip(c,-1,1)))
def fitmoon(T,code,parent,ser,pole=None):
    r=T[code];g=lambda k:f_(r.get(k))
    a,e,inc=g('a (km)'),g('e'),g('i (deg)');P=g('P (days)');pa,pn=g('P apsis (yr)'),g('P node (yr)')
    ra,dec=g('R.A. (deg)'),g('Dec. (deg)')
    if ra is None and parent in POLES:ra,dec=pole or POLES[parent]
    F=frame(ra,dec);ep=r['ep'];arr=np.array(ser);t=arr[:,0]-2451545.0;H=arr[:,1:4];Hn=H/np.linalg.norm(H,axis=1)[:,None]
    def res(q,full):
        p=list(q)+[0]*(10-len(q)) if not full else q
        m=model(p,t,a,e,inc,F);m=m/np.linalg.norm(m,axis=1)[:,None];return (m-Hn).ravel()
    best=None
    for pm in ('anom','sidereal'):
        for ws in (1,-1,0):
            for ns in (1,-1,0):
                wd=(360/(pa*365.25) if pa else 0)*ws;od=-(360/(pn*365.25) if pn else 0)*ns
                n=360/P+(-wd-od if pm=='sidereal' else 0);dt=2451545.0-ep
                p0=[g('M (deg)')+n*dt,n,g('ω (deg)')+wd*dt,wd,g('node (deg)')+od*dt,od]
                try:s=least_squares(lambda q:res(q,False),p0,method='lm',max_nfev=2000)
                except Exception:continue
                rms=float(np.sqrt(np.mean(angerr(list(s.x)+[0,0,0,0],t,a,e,inc,F,H)**2)))
                if best is None or rms<best[0]:best=(rms,list(s.x)+[0,0,0,0])
    rms,p=best
    if rms>0.5:   # add a slow quadratic drift and one libration term if they help
        cands=[]
        s=least_squares(lambda q:res(q,False),p[:7],method='lm',max_nfev=3000);p7=list(s.x)+[0,0,0]
        cands.append((float(np.sqrt(np.mean(angerr(p7,t,a,e,inc,F,H)**2))),p7))
        for Ty in (2,5,10,20,40,70,120,250):
            for A0 in (5,20,45):
                q0=p7[:7]+[A0,2*math.pi/(Ty*365.25),0]
                try:s=least_squares(lambda q:res(q,True),q0,method='lm',max_nfev=3000)
                except Exception:continue
                q=list(s.x);cands.append((float(np.sqrt(np.mean(angerr(q,t,a,e,inc,F,H)**2))),q))
        c=min(cands,key=lambda x:x[0])
        if c[0]<rms*0.8:rms,p=c
    errs=angerr(p,t,a,e,inc,F,H)
    return dict(p=[float(x) for x in p],rms=float(rms),mx=float(errs.max()),ra=ra,dec=dec,a=a,e=e,i=inc,span=(float(arr[0,0]),float(arr[-1,0])))
def model2(p,t,F):
    a,e,inc=p[10],p[11],p[12];return model(p[:10],t,a,e,inc,F)
def fitmoon2(T,code,parent,ser,pole=None):
    """1) robust phase fit (unwrapped along-track residual) per precession variant, 2) least-squares refine,
       3) optional libration term, 4) for poor fits also free a, e, i (best-fit mean ellipse)."""
    r=T[code];g=lambda k:f_(r.get(k))
    a,e,inc=g('a (km)'),g('e'),g('i (deg)');P=g('P (days)');pa,pn=g('P apsis (yr)'),g('P node (yr)')
    ra,dec=g('R.A. (deg)'),g('Dec. (deg)')
    if ra is None and parent in POLES:ra,dec=pole or POLES[parent]
    F=frame(ra,dec);ep=r['ep'];arr=np.array(ser);t=arr[:,0]-2451545.0;H=arr[:,1:4];Hn=H/np.linalg.norm(H,axis=1)[:,None]
    rms_of=lambda p:float(np.sqrt(np.mean(angerr(p[:10],t,p[10],p[11],p[12],F,H)**2)))
    def unit_res(p):m=model2(p,t,F);return (m/np.linalg.norm(m,axis=1)[:,None]-Hn).ravel()
    cands=[]
    for pm in ('anom','sidereal'):
        for ws in (1,-1):
            for ns in (1,-1):
                wd=(360/(pa*365.25) if pa else 0)*ws;od=-(360/(pn*365.25) if pn else 0)*ns
                nb=360/P+(-wd-od if pm=='sidereal' else 0);dt=2451545.0-ep
                base=[g('M (deg)')+nb*dt,nb,g('ω (deg)')+wd*dt,wd,g('node (deg)')+od*dt,od,0,0,0,0,a,e,inc]
                # stage 1: along-track phase, unwrapped, linear+quadratic
                m=model2(base,t,F);N=np.cross(m[0],m[min(3,len(m)-1)]) # rough plane normal
                Nn=np.cross(m,np.roll(m,-1,0)).mean(0);Nn/=np.linalg.norm(Nn)
                res=np.degrees(np.arctan2(np.cross(m,H)@Nn,np.sum(m*H,1)));res=np.degrees(np.unwrap(np.radians(res)))
                for quad in (False,True):
                    A=np.column_stack([np.ones_like(t),t]+([0.5*t*t] if quad else []));c=np.linalg.lstsq(A,res,rcond=None)[0]
                    p=base[:];p[0]+=c[0];p[1]+=c[1];p[6]=c[2] if quad else 0
                    cands.append((rms_of(p),p))
    cands.sort(key=lambda x:x[0]);best=cands[0]
    # stage 2: refine phase and precession (a, e, i fixed to JPL)
    for rm,p in cands[:3]:
        idx=[0,1,2,3,4,5,6]
        def f(q,p=p):pp=p[:];[pp.__setitem__(k,v) for k,v in zip(idx,q)];return unit_res(pp)
        try:s=least_squares(f,[p[k] for k in idx],method='lm',max_nfev=400)
        except Exception:continue
        pp=p[:];[pp.__setitem__(k,v) for k,v in zip(idx,s.x)];rr=rms_of(pp)
        if rr<best[0]:best=(rr,pp)
    # stage 3: libration term (resonant moons), bounded amplitude
    if best[0]>0.5:
        for Ty in (1,1.75,2,5,10,40,70,120):
            p=best[1][:];p[7],p[8],p[9]=20,2*math.pi/(Ty*365.25),0
            idx=list(range(10))
            def f(q,p=p):pp=p[:];[pp.__setitem__(k,v) for k,v in zip(idx,q)];return unit_res(pp)
            try:s=least_squares(f,[p[k] for k in idx],method='lm',max_nfev=400)
            except Exception:continue
            pp=p[:];[pp.__setitem__(k,v) for k,v in zip(idx,s.x)]
            if abs(pp[7])<90 and pp[8]>0 and 2*math.pi/pp[8]/365.25<400:
                rr=rms_of(pp)
                if rr<best[0]*0.8:best=(rr,pp)
    fitted_shape=False
    # stage 4: poor fits (mostly irregular moons): free a, e, i too
    if best[0]>3:
        p=best[1][:];idx=[0,1,2,3,4,5,6,10,11,12]
        def f(q,p=p):pp=p[:];[pp.__setitem__(k,v) for k,v in zip(idx,q)];pp[11]=min(max(pp[11],0),0.95);return unit_res(pp)
        try:
            s=least_squares(f,[p[k] for k in idx],method='lm',max_nfev=600)
            pp=p[:];[pp.__setitem__(k,v) for k,v in zip(idx,s.x)];pp[11]=min(max(pp[11],0),0.95);rr=rms_of(pp)
            if rr<best[0]*0.8:best=(rr,pp);fitted_shape=True
        except Exception:pass
    rr,p=best;errs=angerr(p[:10],t,p[10],p[11],p[12],F,H)
    return dict(p=[float(x) for x in p],rms=float(rr),mx=float(errs.max()),ra=ra,dec=dec,shape=fitted_shape,span=(float(arr[0,0]),float(arr[-1,0])),n=len(arr))
def model3(p,t,F,a,e,inc):
    """p=[M0,n,w0,wd,O0,od,acc,A1,f1,ph1,A2,f2,ph2]"""
    M0,n,w0,wd,O0,od,acc=p[:7];extra=0
    for k in (7,10):
        if len(p)>k+2:extra=extra+p[k]*np.sin(p[k+1]*t+p[k+2])
    q=[M0,n,w0,wd,O0,od,acc,0,0,0];m=model(q,t,a,e,inc,F) if np.isscalar(extra) and extra==0 else None
    if m is not None:return m
    M=np.radians(M0+n*t+0.5*acc*t*t+extra);w=np.radians(w0+wd*t);O=np.radians(O0+od*t);I=math.radians(inc)
    Mw=(M+np.pi)%(2*np.pi)-np.pi;E=kepler_vec(Mw,e);x=a*(np.cos(E)-e);y=a*math.sqrt(1-e*e)*np.sin(E)
    cO,sO,cw,sw,cI,sI=np.cos(O),np.sin(O),np.cos(w),np.sin(w),math.cos(I),math.sin(I)
    P=np.stack([cw*cO-sw*sO*cI,cw*sO+sw*cO*cI,sw*sI],1);Q=np.stack([-sw*cO-cw*sO*cI,-sw*sO+cw*cO*cI,cw*sI],1)
    return (P*x[:,None]+Q*y[:,None])@F.T
def obs_rate(dense):
    """mean rate (deg/day) of the true longitude measured in the instantaneous orbit plane from a dense series"""
    A=np.array(dense);t=A[:,0];H=A[:,1:4];N=np.cross(H[:-1],H[1:]).mean(0);N/=np.linalg.norm(N)
    X=H[0]/np.linalg.norm(H[0]);Y=np.cross(N,X)
    ang=np.unwrap(np.arctan2(H@Y,H@X));c=np.polyfit(t-t[0],np.degrees(ang),1);return c[0]
def fitmoon3(T,code,parent,ser,dense,pole=None):
    r=T[code];g=lambda k:f_(r.get(k))
    a,e,inc=g('a (km)'),g('e'),g('i (deg)');P=g('P (days)');pa,pn=g('P apsis (yr)'),g('P node (yr)')
    ra,dec=g('R.A. (deg)'),g('Dec. (deg)')
    if ra is None and parent in POLES:ra,dec=pole or POLES[parent]
    F=frame(ra,dec);ep=r['ep'];arr=np.array(ser);t=arr[:,0]-2451545.0;H=arr[:,1:4];Hn=H/np.linalg.norm(H,axis=1)[:,None]
    nL=obs_rate(dense)   # observed mean-longitude rate (sign: prograde/retrograde in the orbit's own plane)
    def rms_of(p,sh):return float(np.sqrt(np.mean(angerr3(p,t,F,sh,H)**2)))
    def angerr3(p,t,F,sh,H):
        m=model3(p,t,F,*sh);c=np.sum(m*H,1)/np.linalg.norm(m,axis=1)/np.linalg.norm(H,axis=1);return np.degrees(np.arccos(np.clip(c,-1,1)))
    def unit_res(p,sh):m=model3(p,t,F,*sh);return (m/np.linalg.norm(m,axis=1)[:,None]-Hn).ravel()
    sh0=(a,e,inc);cands=[]
    for ws in (1,-1,0):
        for ns in (1,-1,0):
            wd=(360/(pa*365.25) if pa else 0)*ws;od=-(360/(pn*365.25) if pn else 0)*ns
            for sgn in (1,-1):
                nM=sgn*abs(nL)-wd-od          # mean anomaly rate so that longitude advances at the observed rate
                if abs(nM)<1e-9:continue
                for nn in (nM,360/P,360/P-wd-od):
                    dt=2451545.0-ep;base=[g('M (deg)')+nn*dt,nn,g('ω (deg)')+wd*dt,wd,g('node (deg)')+od*dt,od,0]
                    m=model3(base,t,F,*sh0);m2=model3(base,t+abs(360/nn)/50,F,*sh0)   # orbit normal at each sample, from the model itself
                    Nn=np.cross(m,m2);Nn/=np.linalg.norm(Nn,axis=1)[:,None]
                    res=np.degrees(np.unwrap(np.arctan2(np.sum(Nn*np.cross(m,H),1),np.sum(m*H,1))))
                    for quad in (False,True):
                        A=np.column_stack([np.ones_like(t),t]+([0.5*t*t] if quad else []));c=np.linalg.lstsq(A,res,rcond=None)[0]
                        p=base[:];p[0]+=c[0];p[1]+=c[1];p[6]=c[2] if quad else 0;cands.append((rms_of(p,sh0),p))
    cands.sort(key=lambda x:x[0]);best=(cands[0][0],cands[0][1],sh0)
    for rm,p in cands[:4]:
        try:s=least_squares(lambda q:unit_res(q,sh0),p,method='lm',max_nfev=500)
        except Exception:continue
        rr=rms_of(list(s.x),sh0)
        if rr<best[0]:best=(rr,list(s.x),sh0)
    # periodic terms (resonances, solar perturbations of distant moons): up to two, periods searched
    Pplan={'mars':687,'jupiter':4332.6,'saturn':10759,'uranus':30689,'neptune':60182,'pluto':90560}[parent]
    for nterm in (1,2):
        if best[0]<=0.5:break
        tried=[]
        for Td in (365.25*1,365.25*1.75,365.25*5,365.25*10,365.25*40,365.25*70,365.25*120,Pplan/2,Pplan,abs(360/nL)*10 if nL else 0):
            if Td<=0:continue
            p=best[1][:]+[15,2*math.pi/Td,0]
            try:s=least_squares(lambda q:unit_res(q,best[2]),p,method='lm',max_nfev=500)
            except Exception:continue
            q=list(s.x);ok=all(abs(q[k])<120 and q[k+1]>0 for k in range(7,len(q),3))
            if ok:tried.append((rms_of(q,best[2]),q))
        if tried:
            c=min(tried,key=lambda x:x[0])
            if c[0]<best[0]*0.85:best=(c[0],c[1],best[2])
            else:break
    shape=False
    if best[0]>3:
        p=best[1][:]+list(best[2])
        def f(q):return unit_res(q[:-3],(q[-3],min(max(q[-2],0),.95),q[-1]))
        try:
            s=least_squares(f,p,method='lm',max_nfev=800);q=list(s.x);sh=(q[-3],min(max(q[-2],0),.95),q[-1]);rr=rms_of(q[:-3],sh)
            if rr<best[0]*0.85 and sh[0]>0:best=(rr,q[:-3],sh);shape=True
        except Exception:pass
    rr,p,sh=best;errs=angerr3(p,t,F,sh,H)
    return dict(p=[float(x) for x in p],shape=[float(x) for x in sh],shapefit=shape,rms=float(rr),mx=float(errs.max()),p95=float(np.percentile(errs,95)),ra=ra,dec=dec,nL=float(nL),span=(float(arr[0,0]),float(arr[-1,0])))
def piecewise(r,ser,years=10):
    """refit the global solution in consecutive windows; returns list of (t_start_days_from_J2000, p, shape, rms, max)"""
    arr=np.array(ser);tt=arr[:,0]-2451545.0;H=arr[:,1:4];F=frame(r['ra'],r['dec'])
    out=[];w=years*365.25;t0=tt[0]
    while t0<tt[-1]-1:
        sel=(tt>=t0-1)&(tt<=t0+w+1)
        if sel.sum()<8:break
        t=tt[sel];Hs=H[sel];Hn=Hs/np.linalg.norm(Hs,axis=1)[:,None]
        p0=r['p'][:7]+[0,0,0];p0=list(p0)   # drop periodic terms; each window has its own phase/rates
        # re-centre phase terms at the window: keep same parameterisation (t from J2000)
        sh=r['shape']
        def res(q):
            m=model3(q[:-3],t,F,q[-3],min(max(q[-2],0),.95),q[-1]);return (m/np.linalg.norm(m,axis=1)[:,None]-Hn).ravel()
        start=r['p'][:]+list(sh)
        best=None
        for init in (start,p0[:7]+list(sh)):
            try:s=least_squares(res,init,method='lm',max_nfev=600)
            except Exception:continue
            q=list(s.x);shq=(q[-3],min(max(q[-2],0),.95),q[-1])
            m=model3(q[:-3],t,F,*shq);c=np.sum(m*Hs,1)/np.linalg.norm(m,axis=1)/np.linalg.norm(Hs,axis=1);e=np.degrees(np.arccos(np.clip(c,-1,1)))
            rr=float(np.sqrt(np.mean(e**2)))
            if best is None or rr<best[0]:best=(rr,q[:-3],shq,float(e.max()))
        out.append((float(t0),[float(x) for x in best[1]],[float(x) for x in best[2]],best[0],best[3]))
        t0+=w
    return out
def hzelems(code,prim,start,stop,step):
    f=f'{S}/hzcache/elem_{code}_{prim}_{start}_{stop}_{step}.json'
    if os.path.exists(f):return json.load(open(f))
    q=dict(format='json',COMMAND=f"'{code}'",EPHEM_TYPE='ELEMENTS',CENTER=f"'@{prim}'",START_TIME=f"'{start}'",STOP_TIME=f"'{stop}'",STEP_SIZE=f"'{step}'",REF_PLANE="'ECLIPTIC'",OUT_UNITS="'KM-D'",CSV_FORMAT="'YES'",TIME_TYPE="'TDB'")
    import time as _t
    r=None
    for k in range(5):
        try:r=json.load(urllib.request.urlopen('https://ssd.jpl.nasa.gov/api/horizons.api?'+urllib.parse.urlencode(q),timeout=300))['result']
        except Exception:r=None
        if r and ('$$SOE' in r or 'No ephemeris' in r):break
        _t.sleep(5*(k+1))
    if not r:return None
    m=re.search(r'\$\$SOE\s*(.*?)\s*\$\$EOE',r,flags=re.S)
    if not m:return None
    out=[]
    for l in m.group(1).strip().split('\n'):
        c=[x.strip() for x in l.split(',')]
        # JDTDB,Cal,EC,QR,IN,OM,W,Tp,N,MA,TA,A,AD,PR
        out.append(dict(jd=float(c[0]),e=float(c[2]),i=float(c[4]),O=float(c[5]),w=float(c[6]),n=float(c[8]),M=float(c[9]),a=float(c[11])))
    os.makedirs(f'{S}/hzcache',exist_ok=True);json.dump(out,open(f,'w'));return out
def windows_osc(code,prim,ser,years=10,start_jd=None):
    """per-window ecliptic-frame fit, initialised from Horizons osculating elements at the window middle"""
    arr=np.array(ser);tt=arr[:,0]-2451545.0;H=arr[:,1:4];F=np.eye(3);w=years*365.25
    t0=tt[0];mids=[];wins=[]
    while t0<tt[-1]-1:wins.append(t0);t0+=w
    # osculating elements at each window middle (one Horizons call)
    jd0=2451545.0+wins[0]+w/2;jd1=2451545.0+wins[-1]+w/2
    els=hzelems(code,prim,f'JD{jd0:.1f}',f'JD{jd1+1:.1f}',f'{w:.0f} d') if len(wins)>1 else hzelems(code,prim,f'JD{jd0:.1f}',f'JD{jd0+1:.1f}','1 d')
    if not els:return None
    out=[]
    for k,t0 in enumerate(wins):
        sel=(tt>=t0-1)&(tt<=t0+w+1)
        if sel.sum()<6:continue
        o=els[min(k,len(els)-1)];tm=o['jd']-2451545.0
        t=tt[sel];Hs=H[sel];Hn=Hs/np.linalg.norm(Hs,axis=1)[:,None]
        n=o['n'];init=[o['M']-n*tm,n,o['w'],0,o['O'],0,0,o['a'],o['e'],o['i']]
        def res(q):
            m=model3(q[:7],t,F,q[7],min(max(q[8],0),.98),q[9]);return (m/np.linalg.norm(m,axis=1)[:,None]-Hn).ravel()
        try:s=least_squares(res,init,method='lm',max_nfev=800);q=list(s.x)
        except Exception:q=init
        sh=(q[7],min(max(q[8],0),.98),q[9]);m=model3(q[:7],t,F,*sh)
        e=np.degrees(np.arccos(np.clip(np.sum(m*Hs,1)/np.linalg.norm(m,axis=1)/np.linalg.norm(Hs,axis=1),-1,1)))
        out.append(dict(t0=float(t0),p=[float(x) for x in q[:7]],shape=[float(x) for x in sh],rms=float(np.sqrt(np.mean(e**2))),mx=float(e.max())))
    return out
def fit_window(code,prim,tt,H,t0,t1):
    sel=(tt>=t0-1)&(tt<=t1+1)
    if sel.sum()<6:return None
    t=tt[sel];Hs=H[sel];Hn=Hs/np.linalg.norm(Hs,axis=1)[:,None];F=np.eye(3)
    best=None
    for tm_frac in (0.5,0.25,0.75):
        jd=2451545.0+t0+(t1-t0)*tm_frac
        els=hzelems(code,prim,f'JD{jd:.2f}',f'JD{jd+1:.2f}','1 d')
        if not els:continue
        o=els[0];tm=o['jd']-2451545.0;n=o['n']
        init=[o['M']-n*tm,n,o['w'],0,o['O'],0,0,o['a'],o['e'],o['i']]
        def res(q):
            m=model3(q[:7],t,F,q[7],min(max(q[8],0),.98),q[9]);return (m/np.linalg.norm(m,axis=1)[:,None]-Hn).ravel()
        try:s=least_squares(res,init,method='lm',max_nfev=800);q=list(s.x)
        except Exception:q=init
        sh=(q[7],min(max(q[8],0),.98),q[9]);m=model3(q[:7],t,F,*sh)
        e=np.degrees(np.arccos(np.clip(np.sum(m*Hs,1)/np.linalg.norm(m,axis=1)/np.linalg.norm(Hs,axis=1),-1,1)))
        r=dict(t0=float(t0),t1=float(t1),p=[float(x) for x in q[:7]],shape=[float(x) for x in sh],rms=float(np.sqrt(np.mean(e**2))),mx=float(e.max()),n=int(sel.sum()))
        if best is None or r['rms']<best['rms']:best=r
        if best['rms']<0.3:break
    return best
def adaptive(code,prim,ser,years=10,minyears=1,tol=0.5):
    arr=np.array(ser);tt=arr[:,0]-2451545.0;H=arr[:,1:4];out=[]
    def go(t0,t1):
        r=fit_window(code,prim,tt,H,t0,t1)
        if r is None:return
        if r['rms']>tol and (t1-t0)/365.25>minyears*1.5:
            mid=(t0+t1)/2;go(t0,mid);go(mid,t1)
        else:out.append(r)
    t=tt[0]
    while t<tt[-1]-1:go(t,min(t+years*365.25,tt[-1]));t+=years*365.25
    return out
def fit_window_from(tt,H,t0,t1,init):
    sel=(tt>=t0-1)&(tt<=t1+1)
    if sel.sum()<6:return None
    t=tt[sel];Hs=H[sel];Hn=Hs/np.linalg.norm(Hs,axis=1)[:,None];F=np.eye(3)
    def res(q):m=model3(q[:7],t,F,q[7],min(max(q[8],0),.98),q[9]);return (m/np.linalg.norm(m,axis=1)[:,None]-Hn).ravel()
    try:s=least_squares(res,init,method='lm',max_nfev=400);q=list(s.x)
    except Exception:q=list(init)
    sh=(q[7],min(max(q[8],0),.98),q[9]);m=model3(q[:7],t,F,*sh)
    e=np.degrees(np.arccos(np.clip(np.sum(m*Hs,1)/np.linalg.norm(m,axis=1)/np.linalg.norm(Hs,axis=1),-1,1)))
    return dict(t0=float(t0),t1=float(t1),p=[float(x) for x in q[:7]],shape=[float(x) for x in sh],rms=float(np.sqrt(np.mean(e**2))),mx=float(e.max()),n=int(sel.sum()))
def adaptive2(code,prim,ser,years=10,minyears=2.5,tol=1.0):
    """windows of `years`, split while rms > tol down to `minyears`; each window starts from the previous fit,
       and only if that fails from the osculating orbit JPL Horizons gives for the window"""
    arr=np.array(ser);tt=arr[:,0]-2451545.0;H=arr[:,1:4];out=[];last=[None]
    def solve(t0,t1):
        cands=[]
        if last[0] is not None:
            r=fit_window_from(tt,H,t0,t1,last[0])
            if r:cands.append(r)
        if not cands or cands[0]['rms']>min(tol,3.0):
            r=fit_window(code,prim,tt,H,t0,t1)
            if r:cands.append(r)
        return min(cands,key=lambda r:r['rms']) if cands else None
    def go(t0,t1):
        r=solve(t0,t1)
        if r is None:return
        if r['rms']>tol and (t1-t0)/365.25>minyears*1.5:
            mid=(t0+t1)/2;go(t0,mid);go(mid,t1)
        else:out.append(r);last[0]=r['p']+r['shape']
    t=tt[0]
    while t<tt[-1]-1:go(t,min(t+years*365.25,tt[-1]));t+=years*365.25
    return out
_ELS={}
def fit_window(code,prim,tt,H,t0,t1):
    """window fit started from the nearest of a pre-fetched series of Horizons osculating orbits (one request per moon)"""
    sel=(tt>=t0-1)&(tt<=t1+1)
    if sel.sum()<6:return None
    key=(code,prim)
    if key not in _ELS:_ELS[key]=hzelems(code,prim,f'JD{2451545.0+tt[0]:.1f}',f'JD{2451545.0+tt[-1]:.1f}','228 d') or []
    els=_ELS[key]
    if not els:return None
    t=tt[sel];Hs=H[sel];Hn=Hs/np.linalg.norm(Hs,axis=1)[:,None];F=np.eye(3);best=None
    mids=[t0+(t1-t0)*f for f in (0.5,0.2,0.8)]
    for tm_target in mids:
        o=min(els,key=lambda o:abs(o['jd']-2451545.0-tm_target));tm=o['jd']-2451545.0;n=o['n']
        init=[o['M']-n*tm,n,o['w'],0,o['O'],0,0,o['a'],o['e'],o['i']]
        def res(q):m=model3(q[:7],t,F,q[7],min(max(q[8],0),.98),q[9]);return (m/np.linalg.norm(m,axis=1)[:,None]-Hn).ravel()
        try:s=least_squares(res,init,method='lm',max_nfev=600);q=list(s.x)
        except Exception:q=init
        sh=(q[7],min(max(q[8],0),.98),q[9]);m=model3(q[:7],t,F,*sh)
        e=np.degrees(np.arccos(np.clip(np.sum(m*Hs,1)/np.linalg.norm(m,axis=1)/np.linalg.norm(Hs,axis=1),-1,1)))
        r=dict(t0=float(t0),t1=float(t1),p=[float(x) for x in q[:7]],shape=[float(x) for x in sh],rms=float(np.sqrt(np.mean(e**2))),mx=float(e.max()),n=int(sel.sum()))
        if best is None or r['rms']<best['rms']:best=r
        if best['rms']<0.3:break
    return best
