import requests

r = requests.post('http://10.128.95.91/authenticate/' , data = {'user': '/root/root', 'password' : 'nimbula'} )
print r.json()
if r:
    r = requests.get('http://10.128.95.91/info/')
    print r.json()
