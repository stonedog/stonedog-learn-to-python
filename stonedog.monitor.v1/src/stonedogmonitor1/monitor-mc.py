'''
Created on 2013-2-17

@author: Administrator
'''
from stonedogmonitor1.config.initconfig import ConfigObject,ParseConfig
import subprocess,os,sys
if __name__=='__main__':
    pathName=os.getcwd()
    sys.path.append(pathName)
    print('Select Mode : 1:important province')
    print ('2:normal mode')
    choice=raw_input()
    if choice=='1':
        cfile='d:\\hostimportant.conf'
    else :
        cfile='d:\\host.conf'
    cfs=ParseConfig(cfile)
    for oneHost in cfs:
        args='python one-machine.py '+oneHost.HostName
        print args
        subprocess.Popen(args,creationflags = subprocess.CREATE_NEW_CONSOLE)
    