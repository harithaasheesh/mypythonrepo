import re
x=input("enter string")
n='\D{8,15}'
match=re.fullmatch(n,x)
if match is not None:
    print("valid")
else:
    print("invalid")