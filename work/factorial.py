num=int(input("enter a number"))
if num>0:
  product=1
  for i in range(1,num+1):
      product=product*i
  print("factorial=",product)
elif num==0:
  print("factorial of 0 is 1")
else:
  print("factorial does not exist for -ve number")


# num=int(input("enter a number"))
# product=1
# i=1
# while (i<=num):
#     product=product*i
#     i+=1
# print("factorial=",product)

