class Employee:
    compnay='TCS'
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printvalue(self):
        print(self.name,self.age,Employee.compnay,self.salary)
obj=Employee('asheesh',29,30000)
obj.printvalue()