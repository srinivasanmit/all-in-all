import itertools
#import more_itertools
 
#test = [[-1, -2], [1, 2, 3, [4, (5, [6, 7])]], (30, 40), [25, 35]]
#print(list(more_itertools.collapse(test)))


test = [[-1, -2], [30, 40], [25, 35]]
print list(itertools.chain.from_iterable(test))

print test
t1 = []
[ t1.extend(item) for item in test ]
print t1

def unifylist(l_input, l_target):
    for it in l_input:
        if isinstance(it, list):
            unifylist(it, l_target)
        elif isinstance(it, tuple):
            unifylist(list(it), l_target)
        else:
            l_target.append(it)
    return l_target
 
test =  [[-1, -2], [1,2,3, [4,(5,[6,7])]], (30, 40), [25, 35]]
 
print(unifylist(test,[]))
