import json,math,numpy as np
from smoonfit import *
S=json.load(open('sky_fit.json'));OUT=json.load(open('fits.json'))
rows=S['Namaka'];t=np.array([r['te'] for r in rows]);E=np.array([r['east'] for r in rows]);N=np.array([r['north'] for r in rows]);D=np.array([r['D'] for r in rows]);Ob=np.array([r['mir'] for r in rows])
a,e,i,w,Om,M,ms=25548,0.2137,69.048,117.82,23.606,186.32,1.1e18;nn=math.sqrt(G*(3952.62e18+ms)/a**3)*86400/DEG
T0,T1=t.min(),t.max();L=3*365.25;edges=list(np.arange(T0,T1,L))+[T1];edges[-2:]=[edges[-2],T1] if T1-edges[-2]>L/2 else [T1];edges=sorted(set(edges))
if edges[-1]!=T1:edges.append(T1)
W=[None]*(len(edges)-1);EP=2454615.0
k0=max(j for j in range(len(edges)-1) if edges[j]<=EP)
def fitwin(j,p0,tm0):
    a_,b_=edges[j],edges[j+1];Lw=b_-a_;B=min(.5*Lw,max(min(120,.1*Lw),.15*16));m=(t>=a_-B)&(t<=b_+B);tm=0.5*(a_+b_)
    p=list(p0);p[0]=p0[0]+p0[1]*(tm-tm0)+(p0[7]*0 if len(p0)>7 else 0)
    if len(p0)>7:p[2]=p0[2]+p0[7]*(tm-tm0);p[3]=p0[3]+p0[8]*(tm-tm0)
    p=p[:7];a0=p[4]
    def res(q):
        X=model(q,t[m],tm);sx=np.sum(X*E[m],1)/D[m]*MAS;sy=np.sum(X*N[m],1)/D[m]*MAS;s=a0/D[m]*MAS
        return np.concatenate([(sx-Ob[m,0])/s,(sy-Ob[m,1])/s])
    r=least_squares(res,p,bounds=(LO,HI),x_scale='jac',max_nfev=4000);best=r.x
    r2=least_squares(res,list(best)+[0,0,0],bounds=(LO+[-np.inf]*3,HI+[np.inf]*3),x_scale='jac',max_nfev=4000)
    if np.mean(r2.fun**2)<0.64*np.mean(r.fun**2):best=r2.x
    rr=res(best);k=m.sum();ang=np.hypot(rr[:k],rr[k:])/DEG
    return best,tm,np.sqrt(np.mean(ang**2)),ang.max()
p=[M+nn*(0.5*(edges[k0]+edges[k0+1])-EP),nn,w,Om,a,e,i];tm0=0.5*(edges[k0]+edges[k0+1])
p,tm,rms,mx=fitwin(k0,p,tm0);W[k0]=(p,tm);print(f'window {k0}: {rms:.2f}° typical, {mx:.2f}° worst, w {p[2]%360:.1f} node {p[3]%360:.2f} e {p[5]:.3f}')
for j in list(range(k0+1,len(W)))+list(range(k0-1,-1,-1)):
    src=W[j-1] if j>k0 else W[j+1];q,tm,rms,mx=fitwin(j,list(src[0]),src[1]);W[j]=(q,tm)
    print(f'window {j}: {rms:.2f}° typical, {mx:.2f}° worst, w {q[2]%360:.1f} node {q[3]%360:.2f} e {q[5]:.3f}')
def win(p,t0,t1,tm):
    q=list(p)+[0]*(10-len(p));Mm,n,wm,Om,a,e,i,w1,O1,M2=q;T=tm-J2000
    return [t0-J2000,t1-J2000,Mm-n*T+.5*M2*T*T,n-M2*T,wm-w1*T,w1,Om-O1*T,O1,M2,a,e,i]
OUT['Namaka']['w']=[win(W[j][0],edges[j],edges[j+1],W[j][1]) for j in range(len(W))];OUT['Namaka']['t']=[float(T0),float(T1)]
json.dump(OUT,open('fits.json','w'));print(len(W),'windows')
