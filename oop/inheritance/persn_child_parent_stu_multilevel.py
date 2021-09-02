class Person:
    def printperson(self,name,age):
        self.name=name
        self.age=age
        print("name=",self.name)
        print("age=",self.age)
class Child(Person):
    def printchild(self,clas,rollno):
        self.clas=clas
        self.rollno=rollno
        print("class=",self.clas)
        print("roll no=",self.rollno)
class Parent(Child):
    def printparent(self,job):
        self.job=job
        print("job=",self.job)
class Student(Child):
    def printstudent(self,school,mark):
        self.school=school
        self.mark=mark
        print("school=",self.school)
        print("mark=",self.mark)

pa=Parent()
pa.printperson('asheesh',29)
pa.printchild(2,23)
pa.printparent('acc')
st=Student()
st.printstudent('ss school',97)