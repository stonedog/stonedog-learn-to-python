#encoding=utf-8
class EventManager(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_gMi-EWdqEeKrivXW9ROrTA
    """
    '''
    事件管理�?
    '''
    def __init__(self):
        self.__events_dict={}
    
    def HaveEventHandler(self,p_event_type,p_event_handler):
        if self.__events_dict.has_key(p_event_type):
            return p_event_handler in self.__events_dict[p_event_type]
        else:
            return False
        
    def RegisterEventListener(self,p_event_type,p_event_handler):
        if not self.HaveEventHandler(p_event_type,p_event_handler):
            l_handlers=self.__events_dict.get(p_event_type,[])
            l_handlers.append(p_event_handler)
            self.__events_dict[p_event_type]=l_handlers
    
    def RemoveEventListener(self,p_event_type,p_event_handler):
        if self.HaveEventHandler(p_event_type,p_event_handler):
            l_handlers=self.__events_dict[p_event_type]
            if len(l_handlers)==1:
                self.__events_dict.remove(p_event_type)
            else :
                del l_handlers[p_event_handler]
                self.__events_dict[p_event_type]=l_handlers
    
    def FireEvent(self,p_event):
        l_event_type=p_event.Type;
        l_event_body=p_event.Body
        l_handlers=self.__events_dict[l_event_type]
        for l_one_handler in l_handlers:
            l_one_handler(l_event_body)
    
