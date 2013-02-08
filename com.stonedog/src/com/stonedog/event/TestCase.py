#encoding=utf-8
from EventManager import EventManager
from Student import Student
from Teacher import Teacher
em=EventManager()
s1=Student('S:zhang',em)
t1=Teacher('T:lin',em)
t2=Teacher('T:huang',em)
s1.AskQuestion('who are you')