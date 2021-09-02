import re
x=input("enter string")
n='^[A-Z][a-z0-9\W]*'
match=re.fullmatch(n,x)
if match is not None:
    print("valid")
else:
    print("invalid")