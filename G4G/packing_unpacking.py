# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    print(a, b, c, d)

def packfun(*lst) :
    print lst
 
# Driver Code
my_list = [1, 2, 3, 4]
 
# Unpacking list into four arguments
fun(*my_list)
packfun(1,2,3,4)

args = [3,6]
print range(*args)

# A Python program to demonstrate use
# of packing
 
# This function uses packing to sum
# unknown number of arguments
def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum
 
# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print "%s == %s" %(key,value)
 
greet_me(name="yasoob")
