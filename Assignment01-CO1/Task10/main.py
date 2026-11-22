import time,threading,multiprocessing
N=10000
def work(): return sum(range(100))
t0=time.perf_counter(); ts=[threading.Thread(target=work) for _ in range(20)]; [x.start() for x in ts]; [x.join() for x in ts]; th=time.perf_counter()-t0
print(f"20 thread create+join elapsed: {th:.6f} s")
# Process creation benchmark kept small to avoid unnecessary host load.
t0=time.perf_counter(); ps=[multiprocessing.Process(target=work) for _ in range(5)]; [x.start() for x in ps]; [x.join() for x in ps]; pr=time.perf_counter()-t0
print(f"5 process create+join elapsed: {pr:.6f} s")
print("Interpretation: timings vary by host; processes have separate address spaces, threads share process memory")
