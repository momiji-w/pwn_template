#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("EXECUTABLE", type=str, help="Executable path")
parser.add_argument("--libc", type=str, help="LIBC path")
parser.add_argument("--ip", type=str, help="Remote IP")
parser.add_argument("--port", type=str, help="Remote port")
parser.add_argument("--remote", type=str, help="Remote Address <IP>:<PORT>")
parser.add_argument("--output", type=str, help="Output path")

args = parser.parse_args()

libc = ""
if args.libc:
    libc = "libc = ELF(\"" + args.libc + "\")"

remote_ip = "localhost"
remote_port = "1337"

if args.remote:
    try:
        address = args.remote.split(":")
        remote_ip = address[0]
        remote_port = address[1]
    except:
        print("[!] Error parsing remote address from --remote, make sure to follow this scheme <IP>:<PORT>.")
        exit(1)

if args.ip:
    remote_ip = args.ip

if args.port:
    remote_port = args.port

template = """from pwn import *

sla = lambda delim, data: p.sendlineafter(delim, data)
sa = lambda delim, data: p.sendafter(delim, data)
s = lambda data: p.send(data)
sl = lambda data: p.sendline(data)
r = lambda nbytes: p.recv(nbytes)
ru = lambda data: p.recvuntil(data)
rl = lambda : p.recvline()

"""

template += f"elf = context.binary = ELF(\"{args.EXECUTABLE}\")\n"
template += "\n"
template += "if args.REMOTE:\n"
template += f"   p = remote(\"{remote_ip}\", {remote_port})\n"
template += "else:\n"
template += "   p = process()\n"
template += "\n"
template += """if args.GDB:
    gdb.attach(p, gdbscript="")
"""

if args.output:
    file = open(args.output, "w")
    file.write(template)
    file.close()
else:
    print(template, end="")
