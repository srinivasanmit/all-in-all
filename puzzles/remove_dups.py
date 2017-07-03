lst = [1,1,1,2,2,2,3,3,6,6,6,6,6,7,7,4,4,1,1,1,1,1,1,2,2,2,2,2,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6]
print lst
new_lst = []
for i in lst :
    if i not in new_lst :
        new_lst.append(i)
print new_lst

j = 1
for i in range(1, len(lst)):
    if lst[i] != lst[i-1] :
        lst[j] = lst[i]
        j += 1
lst = lst[0:j]
'''for i in range(j,len(lst)):
    lst.pop()
'''
print lst

'''
i = 1
orig_len = len(lst)
while i <  orig_len :
    if lst[i] == lst[i-1] :
        lst.pop(i)
        orig_len -= 1
        i += 1
        print orig_len, i, lst
print lst
'''
