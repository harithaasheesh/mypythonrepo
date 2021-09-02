class Vehicle:
    def __init__(self,model,regno,color):
        self.model=model
        self.regno=regno
        self.color=color
    def printval(self):
        print("model=",self.model)
        print("regno=",self.regno)
        print("color=",self.color)
    def __str__(self):
        return  self.model   #only string can return using this to string method
    #   return self.model+self.color

ve=Vehicle("ktm",234,'black')
ve.printval()
print(ve)