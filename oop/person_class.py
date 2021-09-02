class Person:
    def setvalue(self,name,age):  #instance variables
        self.name=name
        self.age=age
    def printvalue(self):
        print("name",self.name)
        print("age",self.age)
pe1=Person()
pe1.setvalue("haritha",27)
pe1.printvalue()
pe2=Person()
pe2.setvalue("asheesh",29)
pe2.printvalue()
