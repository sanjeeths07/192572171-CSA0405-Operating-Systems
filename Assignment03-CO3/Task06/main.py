n=6;s=4
for name,cap in [("RAID0",n*s),("RAID1",(n//2)*s),("RAID5",(n-1)*s),("RAID6",(n-2)*s),("RAID10",(n//2)*s)]:print(name,cap,"TB usable")
