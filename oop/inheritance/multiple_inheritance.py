#multiple inheritance
class Person:
    def setvalue(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print("name",self.name)
        print("age",self.age)
        print("address",self.address)
class Child:
    def set(self,clas,school):
        self.clas=clas
        self.school=school
        print("class",self.clas)
        print("school",self.school)
class Student(Person,Child):
    def printv(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print("rollno",self.rollno)
        print("mark",self.mark)
st=Student()
st.setvalue("haritha","27","abc")
st.set(12,"bpc")
st.printv(22,'100')
