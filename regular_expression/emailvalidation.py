import re
x=input("enter your emaiil id")
n='[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}$'
match=re.fullmatch(n,x)
if match is not None:
    print("valid")
else:
    print("invalid")