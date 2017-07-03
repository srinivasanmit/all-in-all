from collections import Counter

# Creating and intializing counters

lst = [1,1,1,2,2,3]
print Counter(lst)
print Counter({1:3, 2:2, 3:1})
print Counter(A='3', B=2, C=1)

coun = Counter()
coun.update(lst)
print coun
coun.update(lst)
print coun
coun.update(['A','B','C'])
print coun

c1 = Counter(A=4,  B=3, C=10)
c2 = Counter(A=10, B=3, C=4)
 
c1.subtract(c2)
print(c1)

# Accessing counters
cnt_obj = Counter(lst)
lst1 = [ "%s = %s" %(key,value) for key,value in cnt_obj.items()]
print lst1
print ["Count of %s is %s" %(key,value) for key,value in cnt_obj.items()]

for key in cnt_obj.keys() :
    print "Count of %s is %s" %(key, cnt_obj[key])

for key,value in cnt_obj.items():
    print key,value

# elements() method - Does not include elements negative and zero count

count_elements = coun.elements()
print count_elements, type(count_elements)
print list(count_elements)

print list(c1.elements())

coun2 = Counter(a=1, b=2, c=3, d=120, e=1, f=219)
print coun2.most_common(3)

for item, count in coun2.most_common(2) :
    print item,count
