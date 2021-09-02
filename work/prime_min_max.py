# min=int(input("enter a minimum range"))
# max=int(input("enter a maximum range"))
# for i in range(min,max+1):
#     if i>1:
#         for a in range(2,i):
#             if i%a==0:
#                 break
#         else:
#                 print(i)
min=int(input("enter a minimum value"))
max=int(input("enetr a max value"))
for i in range(min,max+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
                print(i)


