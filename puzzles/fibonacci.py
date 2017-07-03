no_to_add = 0
final_no = 1000 
fibonacci = [1]
i = 0
while fibonacci[i] < final_no :
    fib_no = no_to_add + fibonacci[i]
    fibonacci.append(fib_no)
    no_to_add = fibonacci[i]
    i += 1
    
print fibonacci
