numb=int(input("enter a number"))
reverse=0
while numb>0:
    reminder=numb%10
    reverse=(reverse*10)+reminder
    numb=numb//10
print("reverse=",reverse)