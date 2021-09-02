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
class Employe(Person,Parent):
    def setv(self,id,salary):
        self.id=id
        self.salary=salary
        print("id",self.id)
        print("salary",self.salary)
te=Employe()
te.setvalue("asheesh",'29','abc')
te.set("mechanical engineer",'alappuzha')
te.setv("2314","30000")