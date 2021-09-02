string=input("enter a string")
b=""
for i in string:
    if i not in b:
     b=b+i
    else:
        print("recursive character in",string,"is",i)
        break
