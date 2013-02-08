'''
Created on 2013-2-2

@author: Administrator
'''
import subprocess
import time
#con1 = subprocess.Popen('pythonw console.py',stdin=subprocess.PIPE)
con2 = subprocess.Popen('python console.py',shell=False,stdin=subprocess.PIPE)
#con1.stdin.write('aaa\n')
con2.stdin.write('bbb\n')
time.sleep(10)
'''
import subprocess
import time
con1 = subprocess.Popen('pythonw console.py',stdin=subprocess.PIPE)
con2 = subprocess.Popen('pythonw console.py',stdin=subprocess.PIPE)
con1.stdin.write('aaa\n')
con2.stdin.write('bbb\n')
time.sleep(10)
'''
'''
import win32console
import sys
win32console.AllocConsole()
sys.stdout = open("CONOUT$", "w", 0) 
while True:
    s= sys.stdin.readline()
    if not s:
        time.sleep(1)
    sys.stdout.write(s)
    sys.stdout.flush()
'''    