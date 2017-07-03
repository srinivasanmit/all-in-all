orig_lst = [2,1,3,4,7,9,24,98]
print orig_lst
def even_at_even_odd_at_odd(i):
    if (orig_lst[i] % 2 ==0 and (i+1)%2 ==0) or (orig_lst[i] % 2 == 1 and (i+1) % 2 == 1) :
        return True
    return False

def swap_with_next_proper_number(i) :
    for j in range(i+1,len(orig_lst)) :
        if (orig_lst[i] % 2) != (orig_lst[j] % 2) :
            orig_lst[i] = orig_lst[j] + orig_lst[i]
            orig_lst[j] = orig_lst[i] - orig_lst[j]
            orig_lst[i] = orig_lst[i] - orig_lst[j]       

for index in range(len(orig_lst)) :
    if not even_at_even_odd_at_odd(index) :
        swap_with_next_proper_number(index)

print orig_lst
        
