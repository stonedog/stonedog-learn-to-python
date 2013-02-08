#encoding=utf-8
class EventAbleObject(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_gMZNEGdqEeKrivXW9ROrTA
    """
    '''
    能够支持事件的基类，能够生成事件和响应事件�?
    '''
    def __init__(self,p_event_manager):
        self.__event_manager=p_event_manager
    
    def AddEventListener(self,p_event_type,p_event_handler):
        self.__event_manager.RegisterEventListener(p_event_type,p_event_handler)
    
    def RemoveEventListener(self,p_event_type,p_event_handler):
        self.__event_manager.RemoveEventListener(p_event_type,p_event_handler)
    
    def FireEvent(self,p_event):
        self.__event_manager.FireEvent(p_event)
        
    
