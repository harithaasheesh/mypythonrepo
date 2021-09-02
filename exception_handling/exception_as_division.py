num1=int(input("enter first number"))
num2=int(input("enter second number"))
try:
    res=num1/num2
    print(res)
except Exception as a:
    print(a.args)