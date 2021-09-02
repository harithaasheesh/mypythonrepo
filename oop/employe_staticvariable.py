class Employee:
    company='TCS'
    def setvalue(self,id,name,age,department):
        self.id=id
        self.name=name
        self.age=age
        self.department=department
    def printvalu(self):
        print("id",self.id)
        print("name",self.name)
        print("age",self.age)
        print("company",Employee.company)
        print("department",self.department)
em=Employee()
em.setvalue(123,'asheesh',29,'MECHANICAL')
em.printvalu()
em.setvalue(234,'anu','33','it')
em.printvalu()