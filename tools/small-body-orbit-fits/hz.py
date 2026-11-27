# JPL Horizons heliocentric state vectors (J2000 ecliptic, AU and AU/day, times in UT), cached per body in hz/<id>.json
import json,os,re,time,urllib.request,urllib.parse
WORK=os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work/sbfit'))
REPO=os.environ.get('SSE_REPO',os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')))
D=os.path.join(WORK,'hz');os.makedirs(D,exist_ok=True)
# the small bodies of index.html: id -> (name, SBDB record id from LINKS, e.g. 's20000001')
def _ids():
    s=open(REPO+'/index.html',encoding='utf8').read();i=s.index('const SB=');d=0
    for j in range(i+9,len(s)):
        d+=s[j]=='[';d-=s[j]==']'
        if d==0:break
    rows=re.findall(r"\['([^']+)',\s*'([^']+)'",s[i:j]);L=json.loads(s[s.index('const LINKS=')+12:s.index(';\n',s.index('const LINKS='))])
    return {k:(n,L[k][1]) for k,n in rows}
IDS=_ids()
# bodies that already meet the accuracy targets with their single SBDB orbit (docs/sources.md#accuracy-targets): not fitted
SKIP={'eris','haumea','makemake','gonggong','sedna','neowise','hyakutake','thatcher'}
def cmd(k):
    n,s=IDS[k]
    if k=='kyy26':return "'DES=1998 KY26;'"
    m=re.match(r'^(\d+P)/',n)
    return f"'DES={m.group(1)};CAP;'" if m else f"'DES={s[1:]};'"
def _get(q):
    base=dict(format='text',COMMAND=None,EPHEM_TYPE='VECTORS',CENTER="'500@10'",REF_PLANE='ECLIPTIC',REF_SYSTEM='J2000',VEC_TABLE="'2'",OUT_UNITS='AU-D',CSV_FORMAT='YES',TIME_TYPE='UT',VEC_LABELS='NO')
    base.update(q)
    for a in range(6):
        try:
            t=urllib.request.urlopen('https://ssd.jpl.nasa.gov/api/horizons.api?'+urllib.parse.urlencode(base),timeout=300).read().decode()
            if '$$SOE' in t:break
        except Exception as e:t='ERR '+str(e)
        time.sleep(3+3*a)
    if '$$SOE' not in t:raise RuntimeError(t[-400:])
    rows=[]
    for l in t.split('$$SOE')[1].split('$$EOE')[0].strip().split('\n'):
        c=[x.strip() for x in l.split(',')];rows.append([float(c[0])]+[float(x) for x in c[2:8]])
    return rows
def load(k):
    f=f'{D}/{k}.json';return {float(r[0]):r for r in json.load(open(f))} if os.path.exists(f) else {}
def save(k,S):json.dump(sorted(S.values()),open(f'{D}/{k}.json','w'))
COV=os.path.join(D,'coverage.json')
def coverage():return json.load(open(COV)) if os.path.exists(COV) else {}
def span(k,start,stop,step):
    S=load(k)
    for a in range(3):
        try:rows=_get(dict(COMMAND=cmd(k),START_TIME=f"'{start}'",STOP_TIME=f"'{stop}'",STEP_SIZE=f"'{step}'"));break
        except RuntimeError as e:
            m=re.search(r'(prior to|after) A\.D\. (\d{4})-(\w{3})-(\d{2})',str(e))
            if not m:raise
            y=int(m.group(2))
            if m.group(1)=='prior to':start=f'{y+1}-01-01'
            else:stop=f'{y-1}-12-31'
    C=coverage();C[k]=[rows[0][0],rows[-1][0]];json.dump(C,open(COV,'w'))
    for r in rows:S[r[0]]=r
    save(k,S);return S
def planet(p,code):
    # a planet's Horizons positions every 30 days, 1800-2050 (for the app's planet errors): <WORK>/planets/<p>.txt
    f=f'{WORK}/planets/{p}.txt';os.makedirs(os.path.dirname(f),exist_ok=True)
    if not os.path.exists(f):
        q=dict(format='text',COMMAND=f"'{code}'",EPHEM_TYPE='VECTORS',CENTER="'500@10'",REF_PLANE='ECLIPTIC',REF_SYSTEM='J2000',START_TIME="'1800-01-01'",STOP_TIME="'2050-12-31'",
               STEP_SIZE="'30 d'",VEC_TABLE="'1'",OUT_UNITS='AU-D',CSV_FORMAT='YES',TIME_TYPE='UT')
        open(f,'w').write(urllib.request.urlopen('https://ssd.jpl.nasa.gov/api/horizons.api?'+urllib.parse.urlencode(q),timeout=300).read().decode())
    return f
def tlist(k,jds,batch=50):
    S=load(k);jds=[j for j in jds if j not in S]
    for b in range(0,len(jds),batch):
        part=jds[b:b+batch];rows=_get(dict(COMMAND=cmd(k),TLIST_TYPE='JD',TLIST=' '.join(f"'{j:.6f}'" for j in part)))
        for r in rows:S[r[0]]=r
    save(k,S);return S
