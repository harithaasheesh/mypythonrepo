def add(num1,num2):
    s=num1+num2
    print("result=",s)
def sub(num1,num2):
    su=num1-num2
    print("result=",su)
def multiply(num1,num2):
    mul=num1*num2
    print("result=",mul)
def division(num1,num2):
    div=num1/num2
    print("result=",div)
def floor_div(num1,num2):
    floor=num1//num2
    print("result=",floor)
def exponent(num1,num2):
    exp=num1**num2
    print("result=",exp)
while(True):
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.FLOOR DIVISION")
    print("6.EXPONENT")
    choice=int(input("enter your choice"))
    num1=int(input("enter first number"))
    num2=int(input("enter second number"))
    if choice==1:
       add(num1,num2)
    elif choice==2:
       sub(num1,num2)
    elif choice==3:
        multiply(num1,num2)
    elif choice==4:
        division(num1,num2)
    elif choice==5:
        floor_div(num1,num2)
    elif choice==6:
        exponent(num1,num2)
    else:
        print("invalid choice")

