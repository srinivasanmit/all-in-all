import sys
lprint = lambda *args : sys.stdout.write(''.join(map(str, args))+"\n")
lprint("one", 2, "thre", 4)
