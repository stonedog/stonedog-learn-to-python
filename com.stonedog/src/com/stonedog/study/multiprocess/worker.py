'''
Created on 2013-2-16

@author: Administrator
'''
import time
import multiprocessing
class Worker(multiprocessing.Process):
    def __init__(self,q):
        multiprocessing.Process.__init__(self)
        self._queue=q
    
    def run(self):
        time.sleep(10)
        obj=self._queue.get()
        print('in subprocess %d' %(multiprocessing.current_process().pid))
        print obj.say()
        