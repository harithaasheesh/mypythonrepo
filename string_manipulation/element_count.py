a="malayalam"
b=input("enter the element to count")
s=0
flag=0
for i in a:
    if i in b:
        s=s+1
        flag=1
if flag==1:
 print("count=",s)
else:
 print("element not present")
