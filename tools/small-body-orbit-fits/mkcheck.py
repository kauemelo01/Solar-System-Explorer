# Independent test dates for one body: 300 random dates, and 300 between the fitter's own samples -> <SSE_WORK>/check/<id>.json
import sys,os,json,random;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));import hz
k=sys.argv[1];train=sorted(hz.load(k));C=hz.coverage();hz.D=os.path.join(hz.WORK,'check');os.makedirs(hz.D,exist_ok=True);a,b=C[k]
random.seed(hash(k)%1000);T=[random.uniform(a,b) for _ in range(300)]
for _ in range(300):
    i=random.randrange(len(train)-1);T.append(train[i]+random.uniform(0.2,0.8)*(train[i+1]-train[i]))
hz.tlist(k,sorted(round(t,6) for t in T if a<=t<=b));print(k,'ok',flush=True)
