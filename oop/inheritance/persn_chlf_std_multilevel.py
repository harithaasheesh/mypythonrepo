class Person:
    def printperson(self,name,age):
        self.name=name
        self.age=age
        print("name=",self.name)
        print("age=",self.age)
class Child(Person):
    def printchild(self,clas):
        self.clas=clas
        print("class=",self.clas)
class Student(Child):
    def printstudent(self,school):
        self.school=school
        print("school=",self.school)
st=Student()
st.printperson('asheesh',29)
st.printchild(2)
st.printstudent('ss school')