print "Squares and cubes using list comprehension"
# List comprehension is generally faster than a combination of using map and lambda

lst = [1,2,3,4,5,6,7,8,9,10]
squares = [ x**2 for x in lst]
cond = [y%2 ==0 for y in lst]
squares_even = [x**2 for x in filter( lambda x : x%2==0, lst)]
cubes = [x**3 for x in lst]
print "Condition check : {0}".format(cond)
print "Squares list : {0}".format(squares)
print "Squares even list : {0}".format(squares_even)
print "Cubes list   : {0}".format(cubes)
print
print "Squares and cubes using map and lambda"
squares = map( lambda x : x**2 , lst)
squares_even = map( lambda x : x**2, filter( lambda x : x%2==0, lst))
cubes_odd = map( lambda x : x**3 , filter( lambda x: x % 2 , lst))
print "Squares list : {0}".format(squares)
print "Squares even list : {0}".format(squares_even)
print "Cubes list   : {0}".format(cubes_odd)


