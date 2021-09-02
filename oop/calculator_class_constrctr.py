class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addition(self):
        self.sum=self.num1+self.num2
        print("result",self.sum)
    def sub(self):
        self.subs=self.num1-self.num2
        print("result",self.subs)
    def multiply(self):
        self.product=self.num1*self.num2
        print("result",self.product)
print("1.ADDITION")
print("2.SUBSTRACTION")
print("3.MULTIPLICATION")
choice=int(input("enter your choice"))
num1=int(input("enter first number"))
num2=int(input("enter second number"))
obj=Calculator(num1,num2)
if choice==1:
    obj.addition()
elif choice==2:
    obj.sub()
elif choice==3:
    obj.multiply()
else:
    print("invalid operation")
