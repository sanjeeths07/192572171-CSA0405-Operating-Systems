segments={"code":(1000,400),"data":(3000,800),"stack":(5000,500)}
for name,off in [("code",20),("data",799),("data",800),("stack",120)]:
 base,limit=segments[name]; print(f"{name}+{off}: "+(f"physical={base+off} VALID" if off<limit else f"SEGMENTATION FAULT (limit={limit})"))
