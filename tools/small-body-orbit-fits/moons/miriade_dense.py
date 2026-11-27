import urllib.request,re,json,time
def get(sysn,ep,nbd,step):
    u=f"https://ssp.imcce.fr/webservices/miriade/api/ephemsys.php?-name=a:{sysn}&-ep={ep}&-nbd={nbd}&-step={step}&-tscale=UTC&-from=sse"
    for a in range(5):
        try:t=urllib.request.urlopen(u,timeout=300).read().decode();break
        except Exception as e:t='';time.sleep(10)
    comp={}
    for tb in re.findall(r'<vot:TABLE (.*?)</vot:TABLE>',t,re.S):
        nm=re.search(r'ComponentName[^>]*value="([^"]+)"',tb).group(1)
        rows=[[float(x) for x in re.findall(r'<vot:TD>(.*?)</vot:TD>',r)[:3]] for r in re.findall(r'<vot:TR>(.*?)</vot:TR>',tb,re.S)]
        comp.setdefault(nm,[]).append(rows)     # one list per orbital solution
    return comp
out={}
for sysn,sat,step in (('Hektor','Skamandrios','0.25d'),('Eurybates','Queta','4d')):
    R=[]
    for y in range(2001,2030,2):
        c=get(sysn,f'{y}-03-01T00:00:00',40,step)
        if sat not in c:print(sysn,y,'no data');continue
        S,P=c[sat][0],c[sysn][0]           # first (default) solution
        R+=[[a[0],a[1]-b[1],a[2]-b[2]] for a,b in zip(S,P)]
    out[sat]=dict(primary=sysn,rows=R);print(sat,len(R),'positions',flush=True)
json.dump(out,open('miriade_dense.json','w'))
