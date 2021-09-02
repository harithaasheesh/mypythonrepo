class Student:
    def print(self,name,age):
        self.name=name
        self.age=age
        print("name=",self.name)
        print("age=",self.age)
class Teacher(Student):
    def print(self,department,school):
        self.department=department
        self.school=school
        print("department=",self.department)
        print("school=",self.school)
t=Teacher()
t.print('it','ssc')

