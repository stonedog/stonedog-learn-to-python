'''
Created on 2013-2-7

@author: Administrator
'''
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
        self._machineConfig=machineConfig
        self._machine=OneServerMachine(self._machineConfig)
        self._machieState={}
    
    def _check(self):
        self._machineState=self._machine.CheckAll(self._machineConfig)
    
    def _report(self):
        report=MachineConsoleReporter.CreateMachineReporter()
        report.Report(self._machineState)
        
    def CheckAndReport(self):
        self._check()
        self._report()
        