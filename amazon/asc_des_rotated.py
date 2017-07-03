def find_asc_des_rotated(lst) :
    asc = False
    des = False
    for i in range(len(lst) -2) :
        if lst[i] > max(lst[i+1], lst[i+2]) :
            des = True
        elif lst[i] < min(lst[i+1], lst[i+2]) :
            asc = True
        elif lst[i] > lst[i+1] and lst[i] < lst[i+2] :
            print "The list is descending and rotated with max element {0}\n".format(max(lst))
            return
        elif lst[i] < lst[i+1]  and lst[i] > lst[i+2] :
            print "The list is ascending and rotated with max element {0}\n".format(max(lst))
            return
    if asc :
        print "The list is ascending and unrotated with max element {0}\n".format(max(lst))
    elif des :
        print "The list is descending and unrotated with max element {0}\n".format(max(lst))
    else :
        print "Wrong input"

asc_input = [1,2,3,4,5,6]
des_input = [6,5,4,3,2,1]
asc_rot_ip = [4,5,6,1,2,3]
des_rot_ip = [3,2,1,6,5,4]

print asc_input
find_asc_des_rotated(asc_input)
print des_input
find_asc_des_rotated(des_input)
print asc_rot_ip
find_asc_des_rotated(asc_rot_ip)
print des_rot_ip
find_asc_des_rotated(des_rot_ip)
