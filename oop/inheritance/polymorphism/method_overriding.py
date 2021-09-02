class Person:
    def printval(self,name):
        self.name=name
        print("inside person method",self.name)
class Child(Person):
    def printval(self,clas):
        self.clas=clas
        print("inside child method",self.clas)
ch=Child()
ch.printval("first")
#CHILD CLASS METHOD OVERRIDES PARENT CLASS METHOD