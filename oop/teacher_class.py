class Teacher:
    college='bpc college'
    def __init__(self,id,name,department):
        self.id=id
        self.name=name
        self.department=department
    def printvalue(self):
        print("id=",self.id)
        print("name=",self.name)
        print("college=",self.college)
        print("department=",self.department)
id=int(input("eneter id"))
name=input("enter name")
department=input("enter department")
te=Teacher(id,name,department)
te.printvalue()