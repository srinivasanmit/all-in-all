input_lst = [1,3,2,4,5,6,7,8,9,10]

def odd_even_segregate_inplace(lst) :
    j = len(lst) - 1
    for i in range(len(lst)) :
        if lst[i] % 2 == 0:
            while lst[j] % 2 == 0 :
                j -= 1
            if i < j :
                lst[i], lst[j] = lst[j], lst[i]
    print lst
        
print input_lst
odd_even_segregate_inplace(input_lst) 
