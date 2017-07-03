import sys
 
x=1001
print(sys.getrecursionlimit())
 
sys.setrecursionlimit(x)
print(sys.getrecursionlimit())
