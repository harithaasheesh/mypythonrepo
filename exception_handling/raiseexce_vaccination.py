age=int(input("enter your age"))
if age<18:
    raise Exception("you are not eligible for vaccination")
else:
    print("eligible for vaccination")