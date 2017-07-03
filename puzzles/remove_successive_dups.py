lst = [1,1,1,2,2,2,1,1,1,1,3,3,6,6,6,6,6,3,3,3,3,3,1,1]
print lst
encountered = -1
new_lst = []
for i in lst :
    if encountered != i :
        new_lst.append(i)
        encountered = i
print new_lst

