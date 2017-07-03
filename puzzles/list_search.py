def in_array(array1, array2):
    lst = []
    array2 = ' '.join([element for element in array2])
    for element in array1:
        if element in array2 :
            lst.append(element)
    return lst

    return any(element in array2 for element in array1)


a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print in_array(a1,a2)
