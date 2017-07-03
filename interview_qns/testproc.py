testProc([1, 2, 3]) # Explicitly passing in a list
testProc()  # Using a default empty list
 
def testProc(n = []):
    # Do something with n
    print n
