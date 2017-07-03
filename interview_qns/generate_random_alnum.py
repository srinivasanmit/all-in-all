import random, string

print ''.join([ random.choice(string.ascii_lowercase + string.digits) for i in range(10) ])
l = [1,2,3,4,5,6,7]
print random.choice(l)
print random.random()
