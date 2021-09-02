class Student:
    def printvalue(self,name,age):
        self.name=name
        self.age=age
        print("name=",self.name)
        print("age=",self.age)
class Teacher(Student):
    def printvalue(self,department):
        self.department=department
        print("department=",self.department)
te=Teacher()
te.printvalue("it")
