import urllib.request,urllib.parse,json,time
M={'Dysnomia':('120136199','20136199',15.79),'Weywot':('120050000','20050000',11.69),'Vanth':('120090482','20090482',9.54),'Dimorphos':('120065803','20065803',0.474),'Menoetius':('120000617','20000617',4.28)}
H=json.load(open('hz_moons.json'))
def q(c,cen,**kw):
    p=dict(format='text',COMMAND=f"'{c}'",EPHEM_TYPE='VECTORS',CENTER=f"'500@{cen}'",REF_PLANE='ECLIPTIC',REF_SYSTEM='J2000',VEC_TABLE="'1'",OUT_UNITS='KM-S',CSV_FORMAT='YES',TIME_TYPE='UT');p.update(kw)
    for a in range(6):
        try:
            t=urllib.request.urlopen('https://ssd.jpl.nasa.gov/api/horizons.api?'+urllib.parse.urlencode(p),timeout=200).read().decode()
            if '$$SOE' in t:return [[float(l.split(',')[0])]+[float(v) for v in l.split(',')[2:5]] for l in t.split('$$SOE')[1].split('$$EOE')[0].strip().split('\n')]
        except Exception:pass
        time.sleep(5+5*a)
    raise RuntimeError(c)
out={}
for n,(c,cen,P) in M.items():
    a,b=H[n]['span'];R=list(H[n]['rows']);t=a+1
    while t+1.5*P<b:
        R+=q(c,cen,START_TIME=f"'JD{t:.5f}'",STOP_TIME=f"'JD{t+1.5*P:.5f}'",STEP_SIZE="'30'");t+=365.25
    R.sort();out[n]=dict(span=[a,b],rows=R);print(n,len(R),'positions',flush=True)
json.dump(out,open('hz_dense.json','w'))
