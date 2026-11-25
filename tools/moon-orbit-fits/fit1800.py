# Fit every planetary moon to JPL Horizons over 1800-2051 (or the part of it Horizons covers); resumable, one JSON per moon in fits1800/
import sys,os,json,time,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
exec(open('fitlib.py').read())
COV=json.load(open('coverage.json'))
MON={'JAN':1,'FEB':2,'MAR':3,'APR':4,'MAY':5,'JUN':6,'JUL':7,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DEC':12}
def iso(s,shift):
    y,m,d=re.match(r'(\d+)-([A-Z]+)-(\d+)',s).groups();from datetime import date,timedelta
    return (date(int(y),MON[m],int(d))+timedelta(days=shift)).isoformat()
def span(name):
    c=COV[name];a,b='1800-01-04','2051-01-01'
    m=re.search(r'prior to A\.D\. (\S+)',c['1800']);a=max(a,iso(m.group(1),2)) if m else a
    m=re.search(r'after A\.D\. (\S+)',c['2051']);b=min(b,iso(m.group(1),-2)) if m else b
    return a,b
def get(job):
    name,code,prim,par=job;a,b=span(name)
    yrs=(int(b[:4])-int(a[:4]));step='60 d' if yrs>60 else '15 d' if yrs>20 else '5 d'
    ser=hzseries(code,prim,a,b,step)
    return (name,(a,b,step),ser) if ser and len(ser)>20 else (name,None,None)
D='fits1800';os.makedirs(D,exist_ok=True)
fn=lambda n:D+'/'+n.replace('/','_').replace(' ','_')+'.json'
def one2(job):
    name=job[0]
    try:
        n,res=one(job)
        if res is not None and 'error' not in res:res['span']=span(name)
    except Exception as e:res={'error':repr(e)}
    if res is not None:json.dump(res,open(fn(name),'w'))
    return name,res
if __name__=='__main__':
    from concurrent.futures import ProcessPoolExecutor
    todo=[j for j in jobs if not os.path.exists(fn(j[0]))];t0=time.time()
    print('to fit:',len(todo),flush=True)
    with ProcessPoolExecutor(8) as ex:
        for n,res in ex.map(one2,todo):
            k=res.get('kind') if res else None
            info=(f"global rms {res['fit']['rms']:.2f}" if k=='global' else f"{len(res['windows'])} windows, worst {max(w['rms'] for w in res['windows']):.2f}" if k=='windows' and res['windows'] else str(res)[:80])
            print(f"{n}: {info} ({time.time()-t0:.0f}s)",flush=True)
    print('done',flush=True)
