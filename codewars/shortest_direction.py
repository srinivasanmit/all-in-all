def dirReduc(arr):
    dir_dict = {'NORTH':'SOUTH', 'SOUTH':'NORTH', 'EAST':'WEST', 'WEST':'EAST'}
    #return [arr.remove(i) and arr.remove(dir_dict[i]) if dir_dict[i] in arr for i in arr]
    print arr
    for i in arr:
        if dir_dict[i] in arr:
            print i, dir_dict[i]
            arr.remove(i)
            print arr
            arr.remove(dir_dict[i])
            print arr
    return arr

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print "Result -----> ",dirReduc(a)
u=["NORTH", "WEST", "SOUTH", "EAST"]
print "Result -----> ", dirReduc(u)

