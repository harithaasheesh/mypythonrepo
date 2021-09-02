class Person:
    def setvalue(self,id,name):
        self.id=id
        self.name=name
    def printvalue(self):
        print("id=",self.id)
        print("name=",self.name)
class Employee(Person):
    def details(self,salary,department):
        self.salary=salary
        self.department=department
        print("salary=",salary)
        print("department=",department)
id=int(input("enter id"))
name=input("enter name")
salary=int(input("enter salary"))
department=input("enter department")
# pe=Person()
# pe.setvalue(id,name)
# pe.printvalue()
em=Employee()
em.setvalue(id,name)
em.printvalue()
em.details(salary,department)