import re
n=input("enter string")
x='^[A-Z][a-zA-Z0-9]{3,8}[A-Z]$'
matcher=re.fullmatch(x,n)
if matcher is not None:
    print('valid')
else:
    print("invalid")