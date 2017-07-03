d = dict()
d["first"] = "srini"
d["last"] = "vasan"
print "print d {0}".format(d)
print "keys : {0}".format(d.keys())
print "Iterating over the dict"
for i in d :
    print "{0} : {1}".format(i, d[i])
for k,v in d.items() :
    print "{0} -- {1}".format(k, v)
for key in d.keys() :
    print "{0} -- {1}".format(key, d[key])
print 'last' in d.keys()  # is same as 'last' in d
print 'last' in d
print 'vasan' in d
del d['last']
print 'last' in d.keys()
print 'last' in d
print 'vasan' in d



