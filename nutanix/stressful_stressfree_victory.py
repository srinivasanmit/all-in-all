print "Enter score : ",
lst = raw_input().split(':')
a, b = int(lst[0]), int(lst[1])
if b > a :
    a, b = b, a
    print "B's Stressfree and stressful victory score permutations"
else :
    print "A's Stressfree and stressful victory score permutations"

print [(i,j) for i in range(a+1) for j in range(b+1) if i > j and a > b ]
stressful = [(i,j) for i in range(a+1) for j in range(b+1) if i <= j and a > b ]
for i in range(b+1, a+1) :
    stressful.append((i,b))
print stressful
