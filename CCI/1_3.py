s = 'aabbbbcccabcababcccddefggghgghefg'

def dedupe(l1) :
    seen = set()
    for item in l1 :
        if item not in seen :
            yield item
            seen.add(item)

print "".join(dedupe(list(s)))

print "".join(set(s))
