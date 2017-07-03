import os
lst = [1,1,1,0,0,0,3,3,5,5,5,5]

from collections import Counter ;print Counter(lst)

print  dict([[x , lst.count(x)] for x in set(lst)])
print os.path.abspath(__file__)
