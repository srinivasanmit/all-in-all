myvar = 'String variable'
if type(myvar).__name__ == 'str':
    print "myvar is a string!"
elif type(myvar).__name__ == 'list':
    print "myvar is a list!"
