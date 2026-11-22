import ctypes, subprocess, tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as d:
 p=Path(d); (p/"mathlib.c").write_text("int secure_add(int a,int b){return a+b;}\n")
 subprocess.run(["gcc","-shared","-fPIC","-o",str(p/"libmathlib.so"),str(p/"mathlib.c")],check=True)
 lib=ctypes.CDLL(str(p/"libmathlib.so")); lib.secure_add.argtypes=[ctypes.c_int,ctypes.c_int]; lib.secure_add.restype=ctypes.c_int
 print("Runtime-loaded shared library:",p/"libmathlib.so")
 print("dlsym-equivalent symbol secure_add(19,23)=",lib.secure_add(19,23))
 print("Shared object size:",(p/"libmathlib.so").stat().st_size,"bytes")
 print("Address binding: runtime loader maps position-independent shared object into process address space")
