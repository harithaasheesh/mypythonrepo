class Employee:
    def setvalue(self,id,name,age,company,department):
        self.id=id
        self.name=name
        self.age=age
        self.company=company
        self.department=department
    def printvalu(self):
        print("id",self.id,"\n","name",self.name,"\n","age",self.age,"\n","company",self.company,"\n","department",self.department)
em=Employee()
em.setvalue(234,"haritha",27,"TCS","IT")
em.printvalu()