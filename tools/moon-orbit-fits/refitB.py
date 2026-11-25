# Refit distant irregular moons that are more than 3 deg off: 10-year windows that may split down to 2.5 years
# while a window is more than 2 deg off. Keeps whichever of the old and new fits is better on its own training data.
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
exec(open('fit1800.py').read().rsplit("\nif __name__=='__main__':",1)[0])
JOB={j[0]:j for j in jobs};A=set(['Tethys','Telesto','Calypso','Helene','Polydeuces','Methone','Naiad','S/2025 U 1','S/2009 S 2','Janus','Epimetheus'])
V=json.load(open('validate.json'))
todo=[n for n,x in V.items() if x['rms']>3 and n not in A]
def train_rms(res):
    if res['kind']=='global':return res['fit']['rms']
    W=res['windows'];return (sum(w['n']*w['rms']**2 for w in W)/sum(w['n'] for w in W))**.5   # overall rms over all training points
def b1(name):
    job=JOB[name];_,code,prim,par=job;n,s,ser=get(job);old=json.load(open(fn(name)))
    w=adaptive2(code,prim,ser,10,2.5,2.0)
    if not w:return name,None,old
    new=dict(kind='windows',windows=w,span=span(name),note='windows split to 2.5 years')
    return name,new,old
if __name__=='__main__':
    from concurrent.futures import ProcessPoolExecutor
    print('to refit:',len(todo),flush=True)
    with ProcessPoolExecutor(8) as ex:
        for name,new,old in ex.map(b1,todo):
            if new and train_rms(new)<train_rms(old):json.dump(new,open(fn(name),'w'));print(name,'new',round(train_rms(old),2),'->',round(train_rms(new),2),len(new['windows']),'windows',flush=True)
            else:print(name,'kept',round(train_rms(old),2),flush=True)
