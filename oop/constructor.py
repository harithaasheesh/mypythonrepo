#constructure used:initialise instance variable,
class Person:
    def __init__(self,name,age,address): #constructure
        self.name=name
        self.age=age
        self.address=address
    def printvalue(self):
        print(self.name,self.age,self.address)
obj=Person("anu",26,"abc") #attribute can be called during object creation
obj.printvalue()
