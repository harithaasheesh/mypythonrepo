import re
x=input("enter vehicle number")
n='[k][l][0-9]{2}[a-z]{2}[0-9]{4}$'
match=re.fullmatch(n,x)
if match is not None:
    print("valid")
else:
    print("invalid")
