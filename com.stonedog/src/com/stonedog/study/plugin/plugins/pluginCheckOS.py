'''
Created on 2013-2-15

@author: Administrator
'''
from com.stonedog.study.plugin.baseplugin import AbstractPlugin,CMD_ACTION

class CheckOSPlugin(AbstractPlugin):
    def __init__(self,**kwargs):
        self.Commands={CMD_ACTION:'CheckOS'}
    
    def CheckOS(self,**kwargs):
        print('check OS now')