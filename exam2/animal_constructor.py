class Animal:
    def __init__(self,type,color):
        self.type=type
        self.color=color
    def printvalue(self):
        print("type=",self.type)
        print("color=",self.type)
class Dog(Animal):
    def __init__(self,name,age,type,color):
        self.name=name
        self.age=age
        super().__init__(type,color)
    def printv(self):
        print("name=",self.name)
        print("age=",self.age)
d=Dog('tomy','3','lab','black')
d.printvalue()
d.printv()