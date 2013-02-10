'''
Created on 2013-2-7

@author: Administrator
'''
from stonedog.monitor.common.trace import trace
from stonedog.monitor.machine.machine import OneServerMachine
from stonedog.monitor.report.consolereport import MachineConsoleReporter

class OneMachineChecker(object):
    '''
    classdocs
    '''
    def __init__(self,machineConfig):
        '''
        Constructor
        '''
        trace()
        self._machineConfig=machineConfig
        self._machine=OneServerMachine(self._machineConfig)
        self._machieState={}
    
    def _check(self):
        trace()
        self._machineState=self._machine.CheckAll()
    
    def _report(self):
        trace()
        report=MachineConsoleReporter.CreateMachineReporter()
        report.Report(self._machineState)
        
    def CheckAndReport(self):
        trace()
        self._check()
        self._report()
        