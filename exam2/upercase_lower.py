import re
n=input("enter string")
x='[A-Z]{1}[a-z]+'
matcher=re.fullmatch(x,n)
if matcher is not None:
    print('valid')
else:
    print('invalid')