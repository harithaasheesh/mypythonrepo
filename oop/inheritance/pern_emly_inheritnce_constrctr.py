class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name=",self.name)
        print("age=",self.age)
class Employee(Person):
    def __init__(self,salary,department,name,age):
        super().__init__(name, age)
        self.department=department
        self.salary=salary
    def printv(self):
        print("salary=",self.salary)
        print("departmernt=",self.department)
em=Employee(30000,'it','haritha',27)
em.printval()
em.printv()