def dig_sum_power_successive_n(n,p) :
    digits = 1
    tmp = n
    while tmp // 10 > 0 :
        digits += 1
        tmp //= 10
    print "digits == ", digits
    tmp = n
    tmp1 = 0
    for i in range(1, digits+1) :
        tmp1 += pow((tmp % 10) , (digits-i + p))
        tmp //= 10
    return tmp1
        
def dig_pow(n, p):
    # your code
    returned = dig_sum_power_successive_n(n,p)
    print "returned    ", returned 
    if returned % n == 0 :
        return (returned / n)
    else :
        return -1

print "result 1 ", dig_pow(89, 1)
print "result 2 ", dig_pow(92, 1)
print "result 3 ", dig_pow(46288, 3)

'''
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

def dig_pow(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k

def dig_pow(n, p):
    digit_power = sum(int(x)**pw for pw,x in enumerate(str(n),p))
    if digit_power % n == 0:
        return digit_power / n
    return -1

def dig_pow(n, p):
  s = reduce(lambda acc,(i,c): acc+pow(int(c),p+i), enumerate(str(n)), 0)
  return s/n if s%n==0 else -1

def dig_pow(n, p):
    
    total = 0
    digits = [int(d) for d in str(n)]
    
    for i in digits:
        total += i**p
        p += 1
        
    if total%n == 0:
        return int(total/n)
    else:
        return -1

'''
