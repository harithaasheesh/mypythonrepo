def fact(x):
    if x==1:
        return 1
    elif x==0:
        return 1
    else:
        return x*fact(x-1)
num=int(input("enter the number"))
print("factorial is",fact(num))
