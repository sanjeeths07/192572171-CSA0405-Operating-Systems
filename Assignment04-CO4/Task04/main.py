q=[98,183,37,122,14,124,65,67]; head=53
fc=sum(abs(a-b) for a,b in zip([head]+q,q));print("FCFS order:",q,"movement:",fc)
cur=head;left=q[:];total=0;order=[]
while left:
 x=min(left,key=lambda v:abs(v-cur));total+=abs(x-cur);cur=x;order.append(x);left.remove(x)
print("SSTF order:",order,"movement:",total)
