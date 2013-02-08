#encoding=utf-8
from EventAbleObject import EventAbleObject
from Event import Event
class Student(EventAbleObject):
    """
     # PyUML: Do not remove this line! # XMI_ID:_gMsvFWdqEeKrivXW9ROrTA
    """
    def __init__(self,p_name,p_event_manager):
        self.__name=p_name
        super(Student,self).__init__(p_event_manager)
        self.__event_type=Event.StudentAsk
        
    def AskQuestion(self,p_question):
        print ('-------------------')
        print('Student %s Ask Question ' %(self.__name))
        self.AddEventListener(Event.TeacherAnswer,self.TeacherRespond)
        l_event_body={}
        self.FireEvent(Event(self.__event_type,l_event_body))
    
    def TeacherRespond(self,p_event):
        print('Thank your response')
        self.RemoveEventListener(self.__event_type,self.TeacherRespond)
        
        
