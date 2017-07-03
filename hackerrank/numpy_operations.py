import numpy

(n, m) = map(int, raw_input().split())
a = []
b = []
for i in range(n) :
    a.append(map(int, raw_input().split()))
for i in range(n) :
    b.append(map(int, raw_input().split()))
print numpy.add(a,b)
print numpy.subtract(a,b)
print numpy.multiply(a,b)
print numpy.divide(a,b)
print numpy.mod(a,b)
print numpy.power(a,b)

