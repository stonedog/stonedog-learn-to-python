#encoding=utf-8
class Event(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_gLWrQWdqEeKrivXW9ROrTA
    """
    def __init__(self,p_event_type,p_event_body):
        self.__type=p_event_type
        self.__body=p_event_body
    
    @property
    def Type(self):
        return self.__type
    @property
    def Body(self):
        return self.__body
    
    StudentAsk='Student Ask Question'
    TeacherAnswer='Teacher Answer Question'
    
