items=[("Monolithic","fast calls; large trusted kernel; driver fault can crash system"),("Layered","clear interfaces; extra crossings may add overhead"),("Microkernel","small kernel; services isolated; message-passing cost"),("Modular","loadable drivers; flexible updates; modules still run in kernel"),("Hybrid","practical performance/features; larger trusted code base")]
for name,tradeoff in items: print(name+":",tradeoff)
print("Recommendation: small microkernel/RTOS for monitors; modular Linux for database host")
