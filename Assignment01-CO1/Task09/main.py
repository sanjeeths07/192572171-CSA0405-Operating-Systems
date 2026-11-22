tiers=[("Registers/cache","sub-ns to few ns","tiny; hot working data"),("RAM","~100 ns","active patient records and process memory"),("NVMe SSD","~10s-100s us","database and MRI working files"),("HDD","~ms","archive and bulk backup"),("Network/object storage","variable ms+","replicated off-site records and long-term archive")]
for name,lat,use in tiers: print(f"{name}: {lat}; {use}")
print("MRI transfer: DMA is preferred for large blocks; interrupts notify completion")
