lst=[1,2,3,4]
index=int(input("enter index"))
try:
    print(lst[index])
except Exception as e:
    print(e.args)