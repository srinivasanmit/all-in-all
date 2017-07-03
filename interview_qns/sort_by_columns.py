data = [("john", 30, 50), ("john", 21, 50), ("arini", 30, 50)]
print data
str_list = sorted(["-".join([str(item) for item in tup]) for tup in data])
#print str_list
sort_list = [item.split('-') for item in str_list]
print sort_list
#print [int(item) for item in tup[i] for i in range(1,len(data[0])) for tup in sort_list]
print [[int(item) for item in tup[1:]] for tup in sort_list]

biodata = [("raj", 100, 27), ("hari", 50, 26), ("kushal", 58, 26)]
biodata = [("john", 30, 50), ("john", 21, 50), ("arini", 30, 50)]
#print data.sort(key=lambda tup:tup[0])
print "\n", biodata
biodata.sort(key=lambda tup: tup[0], reverse=False)
print biodata
