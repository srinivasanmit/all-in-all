orig_lst = [2,1,3,4,7,9,24,98]
odd_lst = []
even_lst = []
new_lst = []
print orig_lst
for i in orig_lst :
    if i % 2 == 0 :
        even_lst.append(i)
    else:
        odd_lst.append(i)

for i in range(len(orig_lst)) :
    if i % 2 == 0 :
        if len(odd_lst) > 0 :
            new_lst.append(odd_lst.pop(0))
        else :
            break
    else :
        if len(even_lst) > 0 :
            new_lst.append(even_lst.pop(0))
        else :
            break
print new_lst
