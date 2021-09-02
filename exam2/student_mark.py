class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def printdata(self):
        print('name=',self.name)
        print('rollno=',self.rollno)
        print('course=',self.course)
        print('mark=',self.mark)
lst=[]
f=open('student','r')
for i in f:
    number=i.rstrip("\n").split(",")
    print(number)
    name=number[0]
    rollno=number[1]
    course=number[2]
    mark=number[3]
    st=Student(name,rollno,course,mark)
    st.printdata()
    lst.append(st)
mark=[]
for s1 in lst:
    mark.append(s1.mark)
print(mark)
for s1 in lst:
    if(s1.mark==max(mark)):
        print(s1.name,s1.rollno,s1.course,s1.mark)
