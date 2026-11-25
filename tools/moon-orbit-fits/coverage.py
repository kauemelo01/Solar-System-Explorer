import sys,json,re,urllib.request,urllib.parse,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
exec(open('fitall.py').read().split('t0=time.time()')[0])
from concurrent.futures import ThreadPoolExecutor
def q(code,prim,start,stop):
    p=dict(format='json',COMMAND=f"'{code}'",EPHEM_TYPE='VECTORS',CENTER=f"'@{prim}'",START_TIME=f"'{start}'",STOP_TIME=f"'{stop}'",STEP_SIZE="'1 d'",VEC_TABLE="'1'")
    for _ in range(3):
        try:return json.load(urllib.request.urlopen('https://ssd.jpl.nasa.gov/api/horizons.api?'+urllib.parse.urlencode(p),timeout=120))['result']
        except Exception as e:err=repr(e)
    return 'FETCHERR '+err
def cov(job):
    name,code,prim,par=job;out={}
    for tag,(a,b) in (('1800',('1800-01-01','1800-01-02')),('2051',('2051-01-01','2051-01-02'))):
        r=q(code,prim,a,b)
        if '$$SOE' in r:out[tag]='ok'
        else:
            m=re.search(r'(No ephemeris[^\n]*|prior to[^\n]*|after[^\n]*A\.D\.[^\n]*)',r);out[tag]=(m.group(1).strip() if m else r[-300:].strip())
    return name,out
with ThreadPoolExecutor(6) as ex:R=dict(ex.map(cov,jobs))
json.dump(R,open('coverage.json','w'),indent=0)
bad={k:v for k,v in R.items() if v['1800']!='ok' or v['2051']!='ok'}
print('moons',len(R),'fully covered 1800-2051:',len(R)-len(bad))
for k,v in list(bad.items())[:15]:print(k,v)
