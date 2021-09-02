class Student:
    def printvalue(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
        print("name=",self.name)
        print("rollno=",self.rollno)
        print("course=",self.course)
        print("mark=",self.mark)
f1=open('student_detls','r')
for i in f1:
    l=i.split(",")
    #print(l)
    name=l[0]
    rollno=l[1]
    course=l[2]
    mark=l[3]
    st=Student()
    st.printvalue(name, rollno, course, mark)