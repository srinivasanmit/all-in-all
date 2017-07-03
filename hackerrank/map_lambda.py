cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = [0, 1]
    for i in range(n-2) :
        l = len(fib)
        fib.append(fib[l - 1] + fib[l-2])
    return fib

print map(cube, fibonacci(int(raw_input())))
