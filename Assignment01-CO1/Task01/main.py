rows=[("Bedside monitor","10 ms alarm deadline","hard real-time response",1),("Records database","continuous availability","cluster + failover",1),("Imaging server","high throughput","multiprocessor OS",2),("Nurse tablet","battery + mobility","handheld OS",3),("Workstation","interactive productivity","desktop OS",4),("Partner link","secure data exchange","distributed services",2)]
print("Hospital OS requirement ranking (1 = highest)")
for name,req,choice,rank in sorted(rows,key=lambda x:x[3]): print(f"{rank}. {name}: {req}; proposed fit: {choice}")
print("Safety-critical: monitor alarm deadline and patient-record integrity/availability")
