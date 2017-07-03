raw_input()
lst = map(int, raw_input().split())
if all(i > 0 for i in lst) and any(str(j) == str(j)[::-1] for j in lst) :
    print "True"
else :
    print "False" 
