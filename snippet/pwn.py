from pwn import *
import sys

arch =  64
challenge = "$1"
libc_path = '$2'

def dbg():
    context.log_level = 'debug'

def echo(content):
    print("\033[4;36;40mOutput prompts:\033[0m" + "\t\033[7;33;40m[*]\033[0m " + "\033[1;31;40m" + content + "\033[0m")

def exp():
    pass

local = int(sys.argv[1])
elf = ELF(challenge)
libc = ELF(libc_path)

context.os = 'linux'
context.terminal = ['tmux', 'splitw', '-h']

if local:
    io = process(challenge,env = {"LD_PRELOAD":libc_path})
else:
    io = remote("node4.buuoj.cn", 25965)

if arch == 64:
    context.arch = 'amd64'
elif arch == 32:
    context.arch = 'i386'

p   = lambda      : pause() 
s   = lambda x    : success(x)
re  = lambda m, t : io.recv(numb=m, timeout=t)
ru  = lambda x    : io.recvuntil(x)
rl  = lambda      : io.recvline()
sd  = lambda x    : io.send(x)
sl  = lambda x    : io.sendline(x)
ia  = lambda      : io.interactive()
sla = lambda a, b : io.sendlineafter(a, b)
sa  = lambda a, b : io.sendafter(a, b)
uu32 = lambda x   : u32(x.ljust(4,b'\x00'))
uu64 = lambda x   : u64(x.ljust(8,b'\x00'))

bps = []
pie = 0

def gdba():
    if local == 0:
        return 0
    cmd ='set follow-fork-mode parent\n'
    if pie:
        base = int(os.popen("pmap {}|awk '{{print $1}}'".format(io.pid)).readlines()[1],16)
        cmd +=''.join(['b *{:#x}\n'.format(b+base) for b in bps])
        cmd +='set $base={:#x}\n'.format(base)
    else:
        cmd+=''.join(['b *{:#x}\n'.format(b) for b in bps])
    gdb.attach(io,cmd)

exp()
ia()
