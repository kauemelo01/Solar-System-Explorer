import sys,json,re,glob,os,time
sys.path.insert(0,os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work')))
from moonmodel import *
from appdata import load
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
REPO=os.environ.get('SSE_REPO',os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..')))
M,MR,SB,CORE,EL,pl=load(REPO+'/index.html')
mid=lambda n:'m-'+re.sub(r'[^a-z0-9]+','-',n.lower())
naif={}
for f in glob.glob(REPO+'/docs/catalogue/moons-*.md'):
    if 'small-bodies' in f:continue
    for l in open(f).read().split('\n'):
        m=re.search(r'<a id="([^"]+)"></a>',l)
        if m and l.startswith('|'):naif[m.group(1)]=[x.strip() for x in l.strip('|').split('|')][7]
PC={'mars':'499','jupiter':'599','saturn':'699','uranus':'799','neptune':'899','pluto':'999'}
jobs=[(x[0],naif[mid(x[0])],PC[x[1]],x[1]) for x in M if x[11] not in('dmoon','hiiaka','namaka','amoon')]
SPANS=[('1950-01-01','2100-01-01','60 d'),('1980-01-01','2060-01-01','30 d'),('2000-01-01','2040-01-01','15 d'),('2010-01-01','2035-01-01','10 d')]
def get(job):
    name,code,prim,par=job
    for s in SPANS:
        ser=hzseries(code,prim,*s)
        if ser and len(ser)>20:return name,s,ser
    return name,None,None
t0=time.time()
with ThreadPoolExecutor(6) as ex:series=list(ex.map(get,jobs))
print('fetched',len(series),'series in',round(time.time()-t0),'s; missing:',[n for n,s,x in series if s is None])
