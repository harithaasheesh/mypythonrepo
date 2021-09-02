import re
n=input("enter string")
x='^a[1-9]+b$'
matcher=re.fullmatch(x,n)
if matcher is not None:
    print('valid')
else:
    print('invalid')