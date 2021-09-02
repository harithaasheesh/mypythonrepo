lst=[2,3,4,5]
index=int(input("enter the index position"))
try:
    print(lst[index])
except:
    print("index not exist in list")
finally:
    print("inside finally")

#try block work every cause
#except block work only exception causes
#finally block work every causes