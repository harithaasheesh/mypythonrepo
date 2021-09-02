#eg: malayalam
# a="abcd"
# b=a[::-1] #reverse
# print(b)
string=input("enter the word to check palindrome")
b=string[::-1]
if string==b:
  print("palindrome")
else:
  print("not palindrome")
