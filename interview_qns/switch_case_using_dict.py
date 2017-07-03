def xswitch(x): 
    return xswitch._system_dict.get(x, None) 
 
xswitch._system_dict = {'files': 10, 'folders': 5, 'devices': 2}
 
print(xswitch('default'))
print(xswitch('devices'))
