# IMCCE Miriade (Genoide) sky-plane offsets of each satellite from its primary, as seen from Earth (mas, UTC): 400 dates over 2022-2031
import urllib.request,re,json,time
SYS={'Haumea':['Hiiaka','Namaka'],'Eurybates':['Queta'],'Hektor':['Skamandrios'],'Quaoar':['Weywot'],'Orcus':['Vanth'],'Patroclus':['Menoetius']}
out={}
for sysn,sats in SYS.items():
  comp={}
  for ep in ('2459580.5','2461280.5'):
    u=f"https://ssp.imcce.fr/webservices/miriade/api/ephemsys.php?-name=a:{sysn}&-ep={ep}&-nbd=200&-step=8.5d&-tscale=UTC&-from=sse"
    for a in range(4):
        try:t=urllib.request.urlopen(u,timeout=300).read().decode();break
        except Exception as e:t="";print("err",e);time.sleep(10)
    if 'vot:TR' not in t:print('no rows:',t[:300])
    tabs=re.findall(r'<vot:TABLE (.*?)</vot:TABLE>',t,re.S)
    for tb in tabs:
        nm=re.search(r'name="ComponentName"[^>]*value="([^"]+)"',tb) or re.search(r'ComponentName[^>]*value="([^"]+)"',tb)
        rows=[[float(x) for x in re.findall(r'<vot:TD>(.*?)</vot:TD>',r)[:3]] for r in re.findall(r'<vot:TR>(.*?)</vot:TR>',tb,re.S)]
        comp.setdefault(nm.group(1),[]).extend(rows)
  if True:
    print(sysn,{k:len(v) for k,v in comp.items()},flush=True)
    P=comp.get(sysn) or list(comp.values())[0]
    for s in sats:
        S=comp[s];out[s]=dict(primary=sysn,rows=[[a[0],a[1]-b[1],a[2]-b[2]] for a,b in zip(S,P)])
json.dump(out,open('miriade.json','w'))
