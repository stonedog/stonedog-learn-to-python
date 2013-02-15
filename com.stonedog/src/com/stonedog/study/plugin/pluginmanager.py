'''
Created on 2013-2-15

@author: Administrator
'''
from com.stonedog.study.plugin.baseplugin import AbstractPlugin,CMD_ACTION

import os,sys

class PluginManager(object):
    def __init__(self,path=None,kwargs={}):
        if path:
            self._pluginPath=path
        else:
            self._pluginPath=os.path.join(os.getcwd(),'plugins')
        
        self._plugins={}
        self._loadPlugins()
        self._registerPlugins()
        
    def _loadPlugins(self):
        sys.path.append(self._pluginPath)
        for fName in os.listdir(self._pluginPath):
            if fName.startswith('plugin') and fName.endswith('py'):
                m=__import__(fName.split('.')[0])
        
    def _registerPlugins(self,**kwargs):
        for cls in AbstractPlugin.__subclasses__():
            obj=cls(**kwargs)
            self._plugins[obj]=obj.Commands
    
    def callPlugin(self,cmd,**kwargs):
        for plugin,commands in self._plugins.items():
            if commands.has_key(cmd):
                getattr(plugin,commands[cmd])(**kwargs)

if __name__=='__main__':
    mgr=PluginManager()
    mgr.callPlugin(CMD_ACTION)