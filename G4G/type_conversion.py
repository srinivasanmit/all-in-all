# Python code to demonstrate Type conversion
# using int(), float()
 
# initializing string
s = "10010"
 
# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)
 
# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)

# initializing string
s = 'geeks'
 
# printing string converting to tuple
c = tuple(s)
print ("After converting string to tuple : ",end="")
print (c)
 
# printing string converting to set
c = set(s)
print ("After converting string to set : ",end="")
print (c)
 
# printing string converting to list
c = list(s)
print ("After converting string to list : ",end="")
print (c)

# initializing integers
a = 1
b = 2
 
# initializing tuple
tup = (('a', 1) ,('f', 2), ('g', 3))
 
# printing integer converting to complex number
c = complex(1,2)
print ("After converting integer to complex number : ",end="")
print (c)
 
# printing integer converting to string
c = str(a)
print ("After converting integer to string : ",end="")
print (c)
 
# printing tuple converting to expression dictionary
c = dict(tup)
print ("After converting tuple to dictionary : ",end="")
print (c)
