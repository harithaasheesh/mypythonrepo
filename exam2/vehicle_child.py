class Vehicle:
    def setvalue(self,model,name):
        self.model=model
        self.name=name
    def printvalue(self):
        print("model=",self.model)
        print("name=",self.name)
class Bus(Vehicle):
    def setv(self,color,no):
        self.color=color
        self.no=no
        print("color=",self.color)
        print("vehicle No=",self.no)
b=Bus()
b.setvalue('XL123','bus')
b.printvalue()
b.setv('white','KL05AC2345')
