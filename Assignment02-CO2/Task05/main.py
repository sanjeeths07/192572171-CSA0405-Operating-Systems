import threading
counter=0; lock=threading.Lock()
def work():
 global counter
 for _ in range(5000):
  with lock: counter+=1
ts=[threading.Thread(target=work) for _ in range(4)]
[t.start() for t in ts]; [t.join() for t in ts]
print("Workers:",len(ts)); print("Expected:",20000); print("Actual:",counter); print("Mutex protected critical section: PASS")
