mark=int(input("enter the mark"))
if mark>=90:
    print("grade=A+")
elif mark<90 and mark>=80:
    print("grade=A")
elif mark<80 and mark>=70:
    print("grade=B+")
elif mark<70 and mark>=60:
    print("garde=B")
elif mark<60 and mark>=50:
    print("grade=C+")
elif mark<50 and mark>=40:
    print("grade=C")
elif mark<40 and mark>=30:
    print("grade=D+")
else:
    print("failed")