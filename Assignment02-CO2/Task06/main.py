alloc=[[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]; mx=[[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]; work=[3,3,2]; need=[[mx[i][j]-alloc[i][j] for j in range(3)] for i in range(5)]; done=[False]*5; seq=[]
while True:
 found=False
 for i in range(5):
  if not done[i] and all(need[i][j]<=work[j] for j in range(3)):
   work=[work[j]+alloc[i][j] for j in range(3)]; done[i]=True; seq.append("P"+str(i)); found=True
 if not found: break
print("Need:",need); print("Safe:",all(done)); print("Sequence:"," -> ".join(seq) if all(done) else "none")
