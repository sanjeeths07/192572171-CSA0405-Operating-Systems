import os
f="syscall_demo.txt";fd=os.open(f,os.O_CREAT|os.O_WRONLY|os.O_TRUNC,0o600);os.write(fd,b"OS system call demo\n");os.close(fd)
fd=os.open(f,os.O_RDONLY);data=os.read(fd,4096);os.close(fd);print("open/write/close then open/read/close");print("Bytes:",len(data));print(data.decode().strip());os.unlink(f)
