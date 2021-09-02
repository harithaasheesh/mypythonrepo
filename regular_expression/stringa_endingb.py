import re
x=input("enter string")
n='^a[a-zA-Z0-9\W]*b$'
match=re.fullmatch(n,x)
if match is not None:
    print("valid")
else:
    print("invalid")