import paramiko

hostname='192.168.123.154'

port=22
username='oracle'
password='oracle'

paramiko.util.log_to_file('d:/paramiko.log')
s=paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(hostname='192.168.123.154',username=username,password=password,port=port)
stdin,stdout,stderror=s.exec_command('df -h')
print stdout.read()
s.close()
