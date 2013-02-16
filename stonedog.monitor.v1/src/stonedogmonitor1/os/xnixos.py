'''
Created on 2013-2-16

@author: Administrator
'''
import paramiko

class XNixHost():
    def __init__(self,cf):
        specialhost=['192.168.1.26','192.168.1.27','192.168.5.31','192.168.5.32']
        self.__cmd='df -h'
        port='22'
        hostname=cf.HostName
        if hostname in specialhost:
            username='oracle'
            password='fj@3919X'
        else:
            username='zhangxiaoming'
            password='25DecXmas25'
        if hostname in ('192.168.5.31','192.168.5.32'):
            self.__cmd='df -Pm' 
 
        self.__host=paramiko.SSHClient()

        self.__host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__host.connect(hostname=hostname,username=username,password=password,port=port)
        
        
    
    def CheckDisk(self):
        stdin,stdout,stderror=self.__host.exec_command(self.__cmd)
        disks=stdout.readlines()
        
        return disks
        
if __name__=='__main__':
    from stonedogmonitor1.config.initconfig import ConfigObject
    cf=ConfigObject()
    cf.HostName='192.168.17.13'
    machine=XNixHost(cf)
    disks=machine.CheckDisk()
    print(type(disks))       
    for dk in disks:
        print dk 