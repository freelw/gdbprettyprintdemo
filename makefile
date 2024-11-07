all:
	g++ -g main.cpp -o crash
clean:
	rm crash
dbg:
	gdb crash -x ./gdbinit