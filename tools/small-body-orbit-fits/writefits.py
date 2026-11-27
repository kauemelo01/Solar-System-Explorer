# fits/*.json -> data/sb-orbits.js (window format of the moons: [t0,t1,M0,n,w0,w',node0,node',M'',a km,e,i], t from J2000 in days)
import json,glob,os,sys
WORK=os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work/sbfit'))
out=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','sb-orbits.js')
g=lambda x,d:float(f'{x:.{d}g}')
F={}
for f in sorted(glob.glob(WORK+'/fits/*.json')):
    k=os.path.basename(f)[:-5];W=json.load(open(f))['w']
    F[k]=[[g(w[0],12),g(w[1],12),g(w[2],13),g(w[3],13),g(w[4],12),g(w[5],8),g(w[6],12),g(w[7],8),g(w[8],8),g(w[9],10),g(w[10],10),g(w[11],10)] for w in W]
s=('// Small-body orbits fitted to JPL Horizons over 1800-2050 AD in time windows (tools/small-body-orbit-fits; docs/sources.md#small-body-orbits).\n'
   '// Each window: [t0, t1 (days from J2000), M0 (deg), n (deg/day), argument of perihelion w0 and rate, node and rate, M\'\' (deg/day^2), a (km), e, i (deg)], J2000 ecliptic.\n'
   'window.SB_FIT='+json.dumps(F,separators=(',',':'))+';\n')
open(out,'w').write(s);print(len(F),'bodies,',sum(len(v) for v in F.values()),'windows,',len(s)//1024,'KB ->',out)
