ps=1024; table={0:5,1:9,2:1,3:4}
for a in [0,100,1024,2048,3500]:
 p,o=divmod(a,ps); print(f"logical={a} page={p} offset={o} "+(f"physical={table[p]*ps+o}" if p in table else "PAGE FAULT"))
print("32-bit / 4KB pages: 2^20 entries"); print("48-bit / 4KB pages: 2^36 entries in a single-level table")
