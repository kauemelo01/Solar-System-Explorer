# Write data/moon-orbits.js for the app from fits1800/*.json
import json,glob,sys,os
J2000=2451545.0
def r(x,d):return float(f"{x:.{d}g}")
def jd(iso):
    from datetime import date
    y,m,d=map(int,iso.split('-'));return date(y,m,d).toordinal()-date(2000,1,1).toordinal()+2451544.5
out={};stats={}
for f in sorted(glob.glob('fits1800/*.json')):
    v=json.load(open(f))
    if not v or 'error' in v:continue
    name=v.get('name') or os.path.basename(f)[:-5]
    a,b=v['span'];t=[round(jd(a)-J2000,1),round(jd(b)-J2000,1)]
    if v['kind']=='global':
        g=v['fit'];p=g['p']
        e={'g':[r(p[0],12),r(p[1],15),r(p[2],12),r(p[3],12),r(p[4],12),r(p[5],12),r(p[6],8)]+[r(x,10) for x in p[7:]],
           's':[r(g['shape'][0],9),r(g['shape'][1],6),r(g['shape'][2],7)],'f':[g['ra'],g['dec']] if g['ra'] is not None else None,'t':t}
        if v.get('c'):e['c']=[round(v['c'][0],3),v['c'][1]]+v['c'][2:]
        stats[name]=dict(kind='g',rms=g['rms'],mx=g['mx'])
    else:
        W=v['windows']
        if not W:continue
        # precision: enough that rounding moves no moon by more than ~0.001 deg over 1800-2050 (checked by validate.js)
        e={'w':[[round(w['t0'],1),round(w['t1'],1),r(w['p'][0],11),r(w['p'][1],14),r(w['p'][2],9),r(w['p'][3],9),r(w['p'][4],9),r(w['p'][5],9),r(w['p'][6],6),r(w['shape'][0],7),r(w['shape'][1],5),r(w['shape'][2],6)] for w in W],'t':t}
        stats[name]=dict(kind='w',rms=max(w['rms'] for w in W),mx=max(w['mx'] for w in W),n=len(W))
    out[name]=e
NAMES=json.load(open('names.json'))   # file stem -> moon name as in the app
out={NAMES.get(k,k):v for k,v in out.items()};stats={NAMES.get(k,k):v for k,v in stats.items()}
js=("// Moon orbits fitted to JPL Horizons ephemerides over 1800-2050, or the part of it Horizons covers (tools/moon-orbit-fits; docs/sources.md#moon-orbits).\n"
    "// g: [M0, n, w0, w', node0, node', M'', (A, f, phase)...] in the plane with pole f (RA, Dec; J2000 ecliptic if null); s: [a km, e, i]; t: fitted span [t0, t1];\n"
    "// c: along-track corrections [t0, step, deg...] added to M, linearly interpolated; w: time windows [t0, t1, M0, n, w0, w', node0, node', M'', a km, e, i] in the J2000 ecliptic frame. t in days from J2000 (TDB), angles in degrees.\n"
    "window.MOON_FIT="+json.dumps(out,separators=(',',':'),ensure_ascii=False)+";\n")
open(sys.argv[1],'w').write(js);json.dump(stats,open('fitstats1800.json','w'),indent=0)
print('moons with fits:',len(out),'| file size',len(js)//1024,'KB')
