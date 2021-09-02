class Person:
    def setvalue(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print("name",self.name)
        print("age",self.age)
        print("address",self.address)
class Parent:
    def set(self,job,place):
        self.job=job
        self.place=place
        print("job",self.job)
        print("place",self.place)
class Teacher(Person,Parent):
    def setv(self,department,school):
        self.department=department
        self.school=school
        print("department",self.department)
        print("school",self.school)
te=Teacher()
te.setvalue("asheesh",'29','abc')
te.set("mechanical engineer",'alappuzha')
te.setv("it","bpc")