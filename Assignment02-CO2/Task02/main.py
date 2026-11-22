jobs=[("J1",0,5),("J2",1,3),("J3",2,1),("J4",3,2)]; q=2; t=0; rem={n:b for n,a,b in jobs}; ready=[]; i=0; done={}; gantt=[]
while len(done)<len(jobs):
 while i<len(jobs) and jobs[i][1]<=t: ready.append(jobs[i][0]); i+=1
 if not ready: t=jobs[i][1]; continue
 p=ready.pop(0); run=min(q,rem[p]); gantt.append((p,t,t+run)); t+=run; rem[p]-=run
 while i<len(jobs) and jobs[i][1]<=t: ready.append(jobs[i][0]); i+=1
 if rem[p]: ready.append(p)
 else: done[p]=t
print("Round Robin quantum=2")
print("Gantt:"," | ".join(f"{p}[{a}-{b}]" for p,a,b in gantt))
for n,a,b in jobs: print(n,"completion",done[n],"turnaround",done[n]-a,"waiting",done[n]-a-b)
