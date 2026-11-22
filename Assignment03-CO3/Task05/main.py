refs=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
def sim(kind,n):
 f=[]; last={}; faults=0
 for i,p in enumerate(refs):
  if p in f: last[p]=i; continue
  faults+=1
  if len(f)<n:f.append(p)
  elif kind=="FIFO":f.pop(0);f.append(p)
  elif kind=="LRU":v=min(f,key=lambda x:last[x]);f[f.index(v)]=p
  else:
   nxt={x:(refs.index(x,i+1) if x in refs[i+1:] else 999) for x in f};v=max(f,key=lambda x:nxt[x]);f[f.index(v)]=p
  last[p]=i
 return faults
for n in (3,4):print(n,"frames FIFO",sim("FIFO",n),"LRU",sim("LRU",n),"Optimal",sim("OPT",n))
b=[1,2,3,4,1,2,5,1,2,3,4,5]
def fifo(a,n):
 f=[];k=c=0
 for p in a:
  if p not in f:
   c+=1
   if len(f)<n:f.append(p)
   else:f[k]=p;k=(k+1)%n
 return c
print("Belady FIFO faults:",fifo(b,3),"(3 frames),",fifo(b,4),"(4 frames)")
