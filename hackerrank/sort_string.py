import re

s = raw_input()
s1 = re.findall(r'[a-z]',s)
s2 = re.findall(r'[A-Z]',s)
s3 = re.findall(r'[1,3,5,7,9]',s)
s4 = re.findall(r'[0,2,4,6,8]',s)
slst = map(sorted, [s1,s2,s3,s4])
astring = reduce(lambda x,y : x+y , slst[0] + slst[1] + slst[2] + slst[3])
print astring
#print sorted(s1 + s2 + s3 + s4)
#lst = s1.extend(s2).extend(s3).extend(s4)
#ns = reduce(lambda x,y : x+y, lst)
#print ns

