lst = [1,2,3,4,5,6,7,8,9,10]
rev = []
for i in range(len(lst)):
    rev += [lst[len(lst) - 1 - i]]
print rev

rev = []
for i in range(len(lst)):
    print lst[-1]
    rev += [lst.pop()]
print rev
print lst
