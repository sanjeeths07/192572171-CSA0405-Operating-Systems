from pathlib import Path
payload=bytes(range(256))*40
Path("records.dat").write_bytes(payload)
for b in (1,512,4096,8192):
 data=Path("records.dat").read_bytes(); reads=(len(data)+b-1)//b; writes=reads
 print(f"buffer={b:4d} bytes read_calls={reads:5d} write_calls={writes:5d} total={reads+writes:5d}")
print("Recommendation: larger buffered blocks reduce syscall count; validate latency and memory budget")
Path("records.dat").unlink()
