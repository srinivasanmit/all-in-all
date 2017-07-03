def small(a, b, c):
    return a if a <= b and a <= c else (b if b <= a and b <= c else c)
    
print(small(1, 0, 1))
print(small(1, 2, 2))
print(small(2, 2, 3))
print(small(5, 4, 3))
