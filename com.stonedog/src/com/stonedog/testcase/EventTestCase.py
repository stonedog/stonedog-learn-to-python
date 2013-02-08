from EventPackage.EventManager import EventManager
from EventPackage.Student import Student
from EventPackage.Teacher import Teacher

em=EventManager()
s1=Student('S:zhang',em)
t1=Teacher('T:lin',em)
t2=Teacher('T:huang',em)
s1.AskQuestion('who are you')