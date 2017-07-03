import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.20.128', username='srini', password='ca$hc0w')
stdin, stdout, stderr = ssh.exec_command('cat ~/Prog/DSAlgo/BST.py')
print type(stdin)
print stdout.read()
print stderr.readlines()
ssh.close()
