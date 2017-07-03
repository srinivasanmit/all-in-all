# A python program to demonstrate the use of 
# cmp(), max(), min()
 
tuple1 = ('python', 'geek')
tuple2 = ('coder', 1)
 
if (cmp(tuple1, tuple2) != 0):
 
    # cmp() returns 0 if matched, 1 when not tuple1 
    # is longer and -1 when tuple1 is shoter
    print('Not the same')
else:
    print('Same')
print ('Maximum element in tuples 1,2: ' +
        str(max(tuple1)) +  ',' +
        str(max(tuple2)))
print ('Minimum element in tuples 1,2: ' +
     str(min(tuple1)) + ','  + str(min(tuple2)))

# Code for converting a list and a string into a tuple
 
list1 = [0, 1, 2]
print(tuple(list1))
print(tuple('python')) # string 'python'

# Code for printing the length of a tuple
 
tuple2 = ('python', 'geek')
print(len(tuple2))

# Code for deleting a tuple
 
tuple3 = ( 0, 1)
del tuple3

tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])
tuple3 = ('python',)*3
print(tuple3)

# Code for concatenating 2 tuples
 
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
 
# Concatenating above two
print(tuple1 + tuple2)

# Code for creating nested tuples
 
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
tuple3 = (tuple1, tuple2)
print(tuple3)

# One way of creation
tup = 'python', 'geeks'
print(tup)
 
# Another for doing the same
tup = ('python', 'geeks')
print(tup)
