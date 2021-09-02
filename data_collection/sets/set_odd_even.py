a={2,3,4,5,6,45,676,88,45,87,60}
odd=set()
even=set()
for i in a:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print("odd numbers",odd)
print("even numbers",even)