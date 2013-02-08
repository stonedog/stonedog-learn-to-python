#encoding=utf-8
from EventAbleObject import EventAbleObject
from Event import Event
class Teacher(EventAbleObject):
    """
     # PyUML: Do not remove this line! # XMI_ID:_gM15AWdqEeKrivXW9ROrTA
    """
    def __init__(self,p_name,p_event_manager):
        self.__name=p_name
        super(Teacher,self).__init__(p_event_manager)
        self.AddEventListener(Event.StudentAsk,self.RespondQuestion)
        
    def RespondQuestion(self,p_event):
        print ('-------------------')
        print('Teacher %s Answer Question' %(self.__name))
        
