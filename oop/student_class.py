#instance variable:inside class and method..related to methods...access using self

class Student:
    school='luminar'  #static variables...related to class..access using class name
    def setvalue(self,rollno,name,clas):
        self.rollno=rollno
        self.name=name
        self.clas=clas
      #  self.school=school
    def printvalue(self):
        print("rollno",self.rollno)
        print("name",self.name)
        print("class",self.clas)
        print("school",Student.school)
st=Student()
# rollno=int(input("enter the rollno"))
# name=input("enetr name")
# clas=int(input("enter class"))
# school=input("enter school")
st.setvalue(1,'anu',3)
st.printvalue()
st1=Student()
st1.setvalue(2,'minu',5)
st1.printvalue()
