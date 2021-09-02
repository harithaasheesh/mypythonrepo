class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age
        print('name=',self.name)
        print('age=',self.age)
class Student:
    def printvalue(self,clas):
        self.clas=clas
        print('class=',self.clas)
class Teacher(Person,Student):
    def printv(self,course):
        self.course=course
        print("course=",self.course)
class Child(Teacher):
    def setv(self,school):
        self.school=school
        print('school=',self.school)
te=Teacher()
te.setvalue('anu',12)
te.printvalue(8)
ch=Child()
ch.setvalue('vinu',6)
ch.printvalue(1)
ch.printv('science')
ch.setv('kvs')
