# planet-fits/*.json -> data/planet-orbits.js (the small bodies' window format: [t0,t1,M0,n,w0,w',node0,node',M'',a km,e,i], t from J2000 in days)
import json,os,sys
WORK=os.environ.get('SSE_WORK',os.path.expanduser('~/solar-system-explorer-work/sbfit'))
out=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','planet-orbits.js')
IDS=['mercury','venus','emb','mars','jupiter','saturn','uranus','neptune','pluto']
g=lambda x,d:float(f'{x:.{d}g}')
F={k:[[g(w[0],12),g(w[1],12),g(w[2],14),g(w[3],14),g(w[4],13),g(w[5],9),g(w[6],13),g(w[7],9),g(w[8],9),g(w[9],12),g(w[10],10),g(w[11],10)] for w in json.load(open(f'{WORK}/planet-fits/{k}.json'))['w']] for k in IDS}
s=('// Planet orbits (and the Earth-Moon barycentre, and Pluto) fitted to JPL Horizons over 1800-2050 AD in time windows (tools/planet-orbit-fits; docs/sources.md#planets).\n'
   '// Each window: [t0, t1 (days from J2000), M0 (deg), n (deg/day), argument of perihelion w0 and rate, node and rate, M\'\' (deg/day^2), a (km), e, i (deg)], heliocentric J2000 ecliptic.\n'
   'window.PL_FIT='+json.dumps(F,separators=(',',':'))+';\n')
open(out,'w').write(s);print(len(F),'bodies,',sum(len(v) for v in F.values()),'windows,',len(s)//1024,'KB ->',out)
