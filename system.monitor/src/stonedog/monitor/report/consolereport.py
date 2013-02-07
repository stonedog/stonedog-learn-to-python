'''
Created on 2013-2-7

@author: Administrator
'''
from consoleprinter import ConsolePrinter
class MachineConsoleReporter(object):
    '''
    classdocs
    '''
    def __init__(self,printer):
        '''
        Constructor
        '''
        self._printer=printer
    
    @staticmethod
    def CreateMachineReporter():
        printer=ConsolePrinter()
        return MachineConsoleReporter(printer)

        
    def Report(self,machineState):
        self._reportHeader()
        self._reportMachine()
        self._reportDB(machineState['DB'])
        self._reportFooter(machineState['OS'])
        
        
    def _reportHeader(self):
        pass
    
    def _reportFooter(self):
        pass
    
    def _reportDB(self,dbState):
        pass
    
    def _reportMachine(self,osState):
        pass
        