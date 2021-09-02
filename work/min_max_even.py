min=int(input("enter a minimum range value"))
max=int(input("enter a maximum range value"))
# for i in range(min,max+1,2):
#     print(i)

# for i in range(min,max+1):
#     if i%2==0:
#         print(i)
#using while loop
while min<=max:
    if min%2==0:
       print(min)
    min+=1