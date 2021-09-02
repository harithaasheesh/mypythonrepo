class Bank:
    def account_creation(self,name,age):
        self.name=name
        self.age=age
    def deposite(self,amount):
        self.amount=amount
        print("balance amount",self.amount)
    def withdraw(self,withdrw):
        self.withdrw=withdrw
        if self.withdrw<self.amount:
            self.amount=self.amount-self.withdrw
            print("balance=",self.amount)
        else:
            print("insufficiant amount")
b=Bank()
name=input("enter name")
age=int(input("enter age"))
amount=int(input("enter the amount to deposite"))
b.account_creation(name,age)
b.deposite(amount)
withdrw=int(input("enter the amount to withdraw"))

b.withdraw(withdrw)