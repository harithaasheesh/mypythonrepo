string=input("enter string")
vowels='aeiou'
new_string=""
for i in string:
    if i not in vowels:
        new_string=new_string+i
print(new_string)