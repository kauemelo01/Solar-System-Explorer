# Horizons positions of the small bodies' moons relative to their primary (km, J2000 ecliptic, UT), 400 random dates within coverage
import urllib.request,urllib.parse,re,json,random,time
M={'Dysnomia':('120136199','20136199'),'Weywot':('120050000','20050000'),'Vanth':('120090482','20090482'),'Dimorphos':('120065803','20065803'),'Menoetius':('120000617','20000617')}
def q(cmd,cen,**kw):
    p=dict(format='text',COMMAND=f"'{cmd}'",EPHEM_TYPE='VECTORS',CENTER=f"'500@{cen}'",REF_PLANE='ECLIPTIC',REF_SYSTEM='J2000',VEC_TABLE="'1'",OUT_UNITS='KM-S',CSV_FORMAT='YES',TIME_TYPE='UT');p.update(kw)
    for a in range(5):
        try:return urllib.request.urlopen('https://ssd.jpl.nasa.gov/api/horizons.api?'+urllib.parse.urlencode(p),timeout=200).read().decode()
        except Exception:time.sleep(5+5*a)
def jd(y,mo,d):
    import datetime;return (datetime.datetime(y,mo,d)-datetime.datetime(2000,1,1,12)).total_seconds()/86400+2451545
MON={m:i+1 for i,m in enumerate('JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC'.split())}
out={}
for n,(c,cen) in M.items():
    a,b=jd(1800,1,1),jd(2051,1,1)
    for _ in range(3):
        t=q(c,cen,START_TIME=f"'JD{a}'",STOP_TIME=f"'JD{b}'",STEP_SIZE="'1000'")
        m=re.search(r'(prior to|after) A\.D\. (\d{4})-(\w{3})-(\d{2})',t)
        if '$$SOE' in t or not m:break
        v=jd(int(m.group(2)),MON[m.group(3).upper()],int(m.group(4)))
        if m.group(1)=='prior to':a=v+1
        else:b=v-1
    random.seed(n);T=sorted(random.uniform(a,b) for _ in range(400));R=[]
    for k in range(0,400,50):
        t=q(c,cen,TLIST_TYPE='JD',TLIST=' '.join(f"'{x:.5f}'" for x in T[k:k+50]))
        for l in t.split('$$SOE')[1].split('$$EOE')[0].strip().split('\n'):
            x=[s.strip() for s in l.split(',')];R.append([float(x[0])]+[float(v) for v in x[2:5]])
    out[n]=dict(span=[a,b],rows=R);print(n,'Horizons covers JD',round(a,1),'-',round(b,1),f'({(a-2451545)/365.25+2000:.0f}-{(b-2451545)/365.25+2000:.0f})',len(R),'dates',flush=True)
json.dump(out,open('hz_moons.json','w'))
