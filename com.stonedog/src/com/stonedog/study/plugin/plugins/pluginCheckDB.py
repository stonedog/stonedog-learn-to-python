'''
Created on 2013-2-15

@author: Administrator
'''
from com.stonedog.study.plugin.baseplugin import AbstractPlugin,CMD_ACTION

class CheckDBPlugin(AbstractPlugin):
    def __init__(self,**kwargs):
        self.Commands={CMD_ACTION:'CheckAll'}
    
    def CheckAll(self,**kwargs):
        print 'Check DB Now'