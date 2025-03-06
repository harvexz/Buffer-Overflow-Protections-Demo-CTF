# Exploit Development Demonstration

This repository contains files used in the demonstration of buffer overflow exploitation on a vulnerable C program, both without and with stack canaries enabled. The goal is to show how stack canaries impact the exploitation process and how, with a format string vulnerability, the canary can be leaked to bypass the protection.

## Files Overview

### **canary.c**

The vulnerable C program source code. It includes:

- A function `vuln()` that reads input unsafely using `gets()`.
- A hidden function `hacked()` that prints a warning and spawns a shell.

### **nocanary**

Binary compiled from `canary.c` **without** stack canaries using the following command:

```bash
gcc canary.c -o nocanary -fno-stack-protector -z execstack -no-pie -m32 -std=c99
```

This binary lacks stack protection, making it vulnerable to straightforward buffer overflow exploitation.

### **canary**

Binary compiled from `canary.c` with stack canaries enabled, using:

```bash
gcc canary.c -o canary -fstack-protector-all -z noexecstack -no-pie -m32 -std=c99
```

This binary has stack canaries.

### **leak\_ip.py**

A Pwntools script used to aid in calculating offset of return address.

### **exploit\_nocanary.py**

A Pwntools script that builds and sends an exploit payload to the `nocanary` binary. The payload overwrites the return pointer to redirect execution to the `hacked()` function.

### **V2exploit\_nocanary.py**

An updated version of the exploit_nocanary.py exploit with further automation.

### **leak.py**

A Pwntools script that leaks canary value using format string vulnerability.

### **exploit\_canary.py**

A Pwntools script that constructs a final exploit payload for the `canary` binary inserting the canary value, bypassing this security method.

## **Demonstration Videos**

The following videos demonstrate the exploitation process:

- **No Canary Semi Manual Exploit:** https://youtu.be/eKUBCukyWmI
- **No Canary Automated Exploit:** https://youtu.be/eKUBCukyWmI
- **Canary Bypass Exploit:** https://youtu.be/rIQPLJq0CSk

