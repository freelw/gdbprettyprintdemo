# gdbprettyprintdemo

1. make
2. make dbg 会使用gdb启动crash
3. 执行 f 4
4. p b

```
@freelw ➜ /workspaces/gdbprettyprintdemo (main) $ make dbg
gdb crash -x ./gdbinit
GNU gdb (Ubuntu 9.2-0ubuntu1~20.04.2) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from crash...
(gdb) r
Starting program: /workspaces/gdbprettyprintdemo/crash 
crash: main.cpp:16: void f1(): Assertion `0' failed.

Program received signal SIGABRT, Aborted.
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
50      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) f 4
#4  0x000055555555517b in f1 () at main.cpp:16
16          assert(0);
(gdb) p b
$1 = dawang_demo with x val 222
(gdb) 

```