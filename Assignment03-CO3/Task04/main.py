mem=100; fault=8_000_000
for rate in [1/1000,1/100000,1/1000000]: print(f"fault_rate={rate:.8f} EAT_ns={(1-rate)*mem+rate*(fault+mem):.2f}")
