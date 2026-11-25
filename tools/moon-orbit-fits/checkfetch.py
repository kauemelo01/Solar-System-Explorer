# Independent check series: Horizons positions on dates the fits did not use (offset 23 d, every 211 d across each moon's span)
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
exec(open('fit1800.py').read().rsplit("\nif __name__=='__main__':",1)[0])
from concurrent.futures import ThreadPoolExecutor
from datetime import date,timedelta
def cf(job):
    name=job[0];_,code,prim,par=job;a,b=span(name)
    a2=(date.fromisoformat(a)+timedelta(days=23)).isoformat()
    yrs=int(b[:4])-int(a[:4]);step='211 d' if yrs>60 else '47 d' if yrs>20 else '11 d'
    return name,hzseries(code,prim,a2,b,step)
with ThreadPoolExecutor(4) as ex:R=dict(ex.map(cf,jobs))
json.dump(R,open('check.json','w'));print('check series:',sum(1 for v in R.values() if v),'of',len(R))
