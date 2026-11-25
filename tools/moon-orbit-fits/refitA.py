# Refit fast inner moons that alias on the 60-day grid: add the dense near-J2000 series to the fit (global), or fit
# daily-sampled 2-year windows (Janus, Epimetheus, which swap orbits every 4 years). Overwrites fits1800/<name>.json.
import sys,os,json,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
exec(open('fit1800.py').read().rsplit("\nif __name__=='__main__':",1)[0])
GLOB=['Tethys','Telesto','Calypso','Helene','Polydeuces','Methone','Naiad','S/2025 U 1','S/2009 S 2']
WIN=['Janus','Epimetheus']
JOB={j[0]:j for j in jobs}
def g1(name):
    job=JOB[name];n,s,ser=get(job);n,dn=dense(job)
    r=fitmoon3(T,job[1],job[3],ser+dn,dn);res=dict(kind='global',fit=r,span=span(name),note='60-d series plus dense near-J2000 series');return name,res
def w1(name):
    job=JOB[name];_,code,prim,par=job;a,b=span(name);ser=[]
    for y0 in range(int(a[:4]),int(b[:4])+1,20):
        s0=max(a,f'{y0}-01-01');s1=min(b,f'{y0+20}-01-01')
        if s0>=s1:continue
        part=hzseries(code,prim,s0,s1,'1 d') or []
        ser+=part[1:] if ser and part and part[0][0]<=ser[-1][0] else part
    w=adaptive2(code,prim,ser,2,0.5,1.0);return name,dict(kind='windows',windows=w,span=span(name),note='daily series, 2-year windows')
if __name__=='__main__':
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(8) as ex:
        futs=[ex.submit(g1,n) for n in GLOB]+[ex.submit(w1,n) for n in WIN]
        for f in futs:
            try:n,res=f.result()
            except Exception as e:print('ERR',repr(e),flush=True);continue
            json.dump(res,open(fn(n),'w'))
            print(n,res['kind'],round(res['fit']['rms'],3) if res['kind']=='global' else (len(res['windows']),round(max(w['rms'] for w in res['windows']),2)),flush=True)
