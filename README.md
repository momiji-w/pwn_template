# Pwn Template

Pwntools template generator written in python.

## Prerequisite:

- python 3.2+ (first ver. that added argparse).

## Usage

```sh
$ ./pwn_template.py [path_to_exe] --libc [path_to_libc] --remote <IP>:<PORT>
```

```python
from pwn import *

sla = lambda delim, data: p.sendlineafter(delim, data)
sa = lambda delim, data: p.sendafter(delim, data)
s = lambda data: p.send(data)
sl = lambda data: p.sendline(data)
r = lambda nbytes: p.recv(nbytes)
ru = lambda data: p.recvuntil(data)
rl = lambda : p.recvline()

elf = context.binary = ELF("./chall")
libc = ELF("./libc.so.6")

if args.REMOTE:
   p = remote("localhost", 5000)
else:
   p = process()

if args.GDB:
    gdb.attach(p, gdbscript="")
```

Read `--help` for more information.
