def likes(names) :
    if not names :
        return 'no one likes this'
    elif len(names) == 1 :
        return '{0} likes this'.format(names[0])
    elif len(names) == 2 :
        return '{0} and {1} like this'.format(names[0],names[1])
    elif len(names) == 3 :
        return '{0}, {1} and {2} like this'.format(names[0], names[1], names[2])
    else :
        return '{0}, {1} and {2} others like this'.format(names[0], names[1], len(names)-2)

print likes([])
print likes(['Peter'])
print likes(['Jacob', 'Alex'])
print likes(['Max', 'John', 'Mark'])
print likes(['Alex', 'Jacob', 'Mark', 'Max'])


'''
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


def likes(names):
    l = len(names)
    s = 'no one likes this'
    
    if l == 1:
        s = names[0] + ' likes this'
    elif l == 2:
        s = ' and '.join(names) + ' like this'
    elif l == 3:
        s = ', '.join(names[:-1]) + ' and ' + names[-1] + ' like this'
    elif l != 0:
        s = ', '.join(names[:2]) + ' and ' + str(l - 2) + ' others like this'
    
    return s

'''
