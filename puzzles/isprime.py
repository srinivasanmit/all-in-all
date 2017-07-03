'''
Check for primality for both decimal inputs and binary inputs
'''

lst = [2, 4, 6, 7, 9, 13, 17, 99, 127, 139]
print lst
prime = []

def is_composite(n) :
    for i in range(2, n/2 + 1) :
        if n % i == 0 :
            return True
    return False

for n in lst :
    if is_composite(n) :
        continue
    else :
        prime.append(n)
print prime

print "Enter number to check for Primality : "
no = raw_input()
if not is_composite(int(no, 2)):
    print "Entered number is prime"
else :
    print "Entered number is composite"
    
