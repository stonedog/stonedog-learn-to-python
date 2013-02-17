'''
Created on 2013-2-16

@author: Administrator
'''
import multiprocessing
import time

class Task():
    def __init__(self,name):
        self._taskName=name
    
    def __call__(self):
        print 'Task %s is handling' % self._taskName

class Result():
    def __init__(self,tName,result):
        self._taskName=tName
        self._result=result
    
    def __call__(self):
        print '%s Result is %s' %(self._taskName,self._result)

class Worker(multiprocessing.Process):
    def __init__(self,taskQueue,resultQueue):
        multiprocessing.Process.__init__(self)
        self._taskQueue=taskQueue
        self._resultQueue=resultQueue
        
    
    def run(self):
        print 'Worker %d running' % self.pid
        while True:
            oneTask=self._taskQueue.get()
            if oneTask is None:
                print 'Worker Completed'
                self._taskQueue.task_done()
                break
            oneTask()
            self._taskQueue.task_done()
            result=Result(oneTask._taskName,self.pid)
            self._resultQueue.put(result)
            time.sleep(1)
'''
class Producer():
    def __init__(self,taskQueue,taskList):
        self._taskList=taskList
        self._taskQueue=taskQueue
    
    def DispatchTask(self):
        for oneTask in self._taskList:
            self._taskQueue.put(oneTask) 
    
    def Finish(self):
        self._taskQueue.put(None)
'''
if __name__=='__main__':
    taskQueue=multiprocessing.JoinableQueue()
    resultQueue=multiprocessing.Queue()
    workerCount=multiprocessing.cpu_count()*2
    
    print('create %d workers' % workerCount)
    
    workers=[Worker(taskQueue,resultQueue) for i in xrange(workerCount)]
    
    for w in workers:
        w.start() 
    
    taskCount=8
    
    for i in xrange(taskCount):
        taskQueue.put(Task(i)) 
         
    
    for i in xrange(workerCount):
        taskQueue.put(None) 
    
    taskQueue.join()
    
    while taskCount:
        
        result=resultQueue.get()
        result()
        taskCount -=1
    