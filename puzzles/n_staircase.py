n = int(raw_input())
for i in range(1, n+1) :
    for j in range(1, n-i+1):
        print "",
    for j in range(1,i+1) :
        print "#",
    print ""

for i in range(1, n+1) :
    for j in range(1, (2*n)-(2*i)+1):
        print '',
    for j in range(1,i+1) :
        print '#',
    print ""

for i in range(1, n+1) :
    print ' '*(n-i),
    print '#'*i
