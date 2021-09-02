class Parent:
    def __init__(self,job,location):
        self.job=job
        self.location=location
    def printvalue(self):
        print("job=",self.job)
        print("location=",self.location)
class Teacher(Parent):
    def __init__(self,name,id,job,location):
        super().__init__(job,location)
        self.name=name
        self.id=id
    def printv(self):
        print("name=",self.name)
        print("id=",self.id)
    def __str__(self):
        return self.job+str(self.id)
te=Teacher('anu',333,'teacher','vaikom')
te.printvalue()
te.printv()
print(te)
