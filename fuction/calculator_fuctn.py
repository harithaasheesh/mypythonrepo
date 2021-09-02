# print("SELECT OPERATION")
# print("1.ADD")
# print("2.SUBSTRACTION")
# print("3.MULTIPLY")
# print("4.DIVISION")
# choice=int(input('enter the choice'))
# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# def sum():
#     s=num1+num2
#     print("result=",s)
# def substraction():
#     minus=num1-num2
#     print("result=",minus)
# def multiply():
#     product=num1*num2
#     print("result=",product)
# def div():
#     division=num1/num2
#     print("result=",division)
# if choice==1:
#  sum()
# elif choice==2:
#  substraction()
# elif choice==3:
#  multiply()
# elif choice==4:
#  div()
# else:
#     print("invalid choice")


def add(x,y):
    return  x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
print("select operation")
print("1.add")
print("2.substraction")
print("3.multiply")
print("4.division")
while True:
    choice=int(input("enter the choice"))
    num1 = int(input("enter first number"))
    num2=int(input("enter second number"))
    if choice==1:
        print(add(num1,num2))
    elif choice==2:
        print(substract(num1,num2))
    elif choice==3:
        print(multiply(num1,num2))
    elif choice==4:
        print(division(num1,num2))
    else:
        print("invalid choice")
