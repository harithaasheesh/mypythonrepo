import re
x=input("enter the word to validate")
n='\w+[0-9]{1}$'
match=re.fullmatch(n,x)
if match is not None:
    print("valid")
else:
    print("invalid")