#1
#2 3
#4 5 6

def numbers():
  n=1
  num=int(input("enter a number"))
  for i in range(0,num):
      for j in range(0,i):
          print(n,end="  ")
          n+=1
      print("\r")
numbers()

#1
#1 2
#1 2 3
#1 2 3 4

# def num(number):
#     for i in range(0,number): #0
#         n=1
#         for j in range(i): #
#             print(n,end=" ")
#             n+=1
#         print()
# num(5)

