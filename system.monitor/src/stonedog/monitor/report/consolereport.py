'''
Created on 2013-2-7

@author: Administrator
'''
from consoleprinter import ConsolePrinter
from stonedog.monitor.common.trace import trace
class MachineConsoleReporter(object):
    '''
    classdocs
    '''
    def __init__(self,printer):
        '''
        Constructor
        '''
        trace()
        self._printer=printer
    
    @staticmethod
    def CreateMachineReporter():
        trace()
        printer=ConsolePrinter()
        return MachineConsoleReporter(printer)

        
    def Report(self,machineState):
        trace()
        self._reportHeader()
        self._reportMachine(machineState['OS'])
        self._reportDB(machineState['DB'])
        self._reportFooter()
        
        
    def _reportHeader(self):
        trace()

    
    def _reportFooter(self):
        trace()

    
    def _reportDB(self,dbState):
        trace()
    
    def _reportMachine(self,osState):
        trace()
        
        