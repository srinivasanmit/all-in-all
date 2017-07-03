from collections import Counter

s = 'aaabbbcccddd'
alpha = 'abcdefghijklmnopqrstuvwxyz'

t = lambda st : max(Counter(st).values()) == 1
print s
print "No duplicates" if t(s) else "Duplicate exists"
print alpha
print "No duplicates" if t(alpha) else "Duplicate exists" 

