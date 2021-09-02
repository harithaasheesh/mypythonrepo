class Sum:
    def addition(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def result(self):
        print("result",self.num1+self.num2)
s=Sum()
num1=int(input("enter first number"))
num2=int(input("enter second number"))
s.addition(num1,num2)
s.result()

