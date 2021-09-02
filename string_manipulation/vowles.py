string=input("enter a string")
vowels="aeiou"
count=0
for i in string:
    if i in vowels:
        count=count+1
    else:
        pass
print("count of vowels=",count)