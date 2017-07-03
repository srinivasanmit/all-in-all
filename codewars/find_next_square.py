import math
def find_next_square(n) :
    sqrt_of_n = int(math.sqrt(n))
    return (sqrt_of_n+1)**2 if sqrt_of_n ** 2 == n else -1

print find_next_square(121)
print find_next_square(625)
print find_next_square(114)
print find_next_square(319225)
print find_next_square(15241383936)
print find_next_square(155)
print find_next_square(342786627)

'''
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

def find_next_square(sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2

'''
