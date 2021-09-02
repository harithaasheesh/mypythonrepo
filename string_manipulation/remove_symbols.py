string=input("enter a string")
punctuations="!@#$%^&*()_|\}{][':;>,<.?/"
no_punct=""
for char in string:
    if char not in punctuations:
        no_punct=no_punct+char
print(no_punct)
