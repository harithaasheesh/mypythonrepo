class Student:
    college='ss colege'
    def __init__(self,name,rollno,department):
        self.name=name
        self.rollno=rollno
        self.department=department
    def printv(self):
        print("name=",self.name)
        print("rollno",self.rollno)
        print("department",self.department)
        print("college",Student.college)
    def __str__(self): #if we want to return int value..convert int to string using str
        return self.name+str(self.rollno)
st=Student('haritha',33,'it')
st.printv()
print(st)