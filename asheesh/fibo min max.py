min=int(input("enter the minimum number"))
max=int(input("enter the maxi number"))
if min==0:
    print("the series is",1)
elif min<0:
    print("invalid input")
else:
 i=min
 m=1
 while i<=max:
  m=m*i
  i=i+1
 print(m)