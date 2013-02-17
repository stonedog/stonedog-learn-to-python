'''
Created on 2013-2-16

@author: Administrator
'''
import worker
import multiprocessing  
class SomeObject():
    def __init__(self,name,sex):
        self._name=name
        self._sex=sex
    
    def say(self):
        print('%s is %s old' %(self._name,self._sex))
        
if __name__=='__main__':
    obj=SomeObject('zhang','30')
    queue=multiprocessing.Queue()
    worker=worker.Worker(queue)
    worker.start()
    queue.put(obj)
    print ('in main process %d' %(multiprocessing.current_process().pid))
    worker.join()