import re,json
def load(path):
    s=open(path).read()
    M=json.loads(re.search(r'const MOONS=(\[.*?\]\]);',s,flags=re.S).group(1))
    mr=s[s.index('const MOON_R={')+len('const MOON_R='):];mr=mr[:mr.index('};')+1]
    mr=re.sub(r'([{,]\s*)([A-Za-z][A-Za-z0-9/ ]*?):',lambda m:m.group(1)+json.dumps(m.group(2))+':',mr)
    MR=json.loads(mr)
    sb=s[s.index('const SB=['):];sb=sb[:sb.index(']];')+2]
    SB=[]
    for m in re.finditer(r"\[\s*'([^']+)',\s*'([^']+)',\s*'([^']+)',\s*'([^']+)',\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*'([^']+)',\s*([^,]+),\s*(\d)\]",sb):
        g=m.groups();SB.append(dict(id=g[0],name=g[1],cat=g[2],kind=g[3],a=eval(g[4]),e=float(g[5]),i=float(g[6]),om=float(g[7]),w=float(g[8]),M0=float(g[9]),ep=float(g[10]),R=float(g[11]),rot=float(g[13])))
    core=s[s.index('const CORE=['):];core=core[:core.index(']];')+2]
    CORE=[]
    for m in re.finditer(r"\['([a-z]+)','([^']+)','([a-z]+)','([^']+)',([0-9.]+),'(#[0-9a-f]+)',([0-9.]+|Infinity),\[([-0-9.]+),([-0-9.]+)\],([-0-9.]+),",core):
        g=m.groups();CORE.append(dict(id=g[0],name=g[1],R=float(g[4]),P=g[6],pole=(float(g[7]),float(g[8])),rot=float(g[9])))
    el=s[s.index('const EL={'):];el=el[:el.index('};')+2]
    EL={k:[float(x) for x in v.split(',')] for k,v in re.findall(r'(\w+):\[([^\]]*)\]',el)}
    pl=re.search(r"add\(\{id:'pluto'[^}]*\}\)",s).group(0)
    return M,MR,SB,CORE,EL,pl
