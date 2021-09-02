lst=[2,3,4,5]
index=int(input("enter index"))
try:
    print(lst[index])
except:
    print("index out of range")
finally:
    print("finally")
