lst = [1,4,3,5,7,6,5,9,11,8]
k = 3
count = 0
pairs = []
print "Input : ", lst
for i in lst :
    if i + k in lst :
        count += 1
        pairs.append((i, i+k))
print "Number of pairs whose difference is {0} = {1} ".format(k,count)
print pairs
