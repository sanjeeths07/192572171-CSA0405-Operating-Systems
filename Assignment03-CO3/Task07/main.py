tasks=[("real-time control",256,"locked/pinned"),("machine learning",1536,"demand-paged"),("logging",128,"buffered")]; total=0
for n,m,mode in tasks: print(n,m,"MB",mode); total+=m
print("Total:",total,"MB of 2048 MB; headroom:",2048-total,"MB")
