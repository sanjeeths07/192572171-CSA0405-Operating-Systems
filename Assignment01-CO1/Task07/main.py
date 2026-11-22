import os
print("Process demonstration")
print(f"PID={os.getpid()} PPID={os.getppid()}")
print("State model: NEW -> READY -> RUNNING -> TERMINATED")
print("PCB: PID, state, registers, program counter, scheduling and memory metadata")
