# a=10
# b=20
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

#second approach
# a=10
# b=30
# (a,b)=(b,a)
# print(a)
# print(b)

#third approach
# a=5
# b=2
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)


a=int(input("eneter the first number"))
b=int(input("enter the second number "))
temp=a
a=b
b=temp
print(a)
print(b)