params = {"server" : "mpilgrim", "uid" : "srini", "database" : "vasan", "password" : "secret"}
print params
list_with_space = ["%s %s" % (k, v) for k, v in params.items()]
print type(list_with_space), list_with_space
list_with_equals = ["%s=%s" % (k,v) for k, v in params.items()]
print type(list_with_equals), list_with_equals
string_with_join = ";".join(["%s=%s" % (k,v) for k,v in params.items()])
print type(string_with_join), string_with_join
string_with_split = string_with_join.split(";")
print type(string_with_split), string_with_split
