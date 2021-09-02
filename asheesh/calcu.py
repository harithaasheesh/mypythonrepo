def select_operation():


 x=input("select a operation")
 a = add()
 b = sub()
 c = mul()
 d = div()

 if x=a:
     print(add)
   def add():
    n1=float(input("enter a number"))
    n2=float(input("enter the number"))
    add=n1+n2
    print(add)
  add()

 def sub():
    n1 = float(input("enter a number"))
    n2 = float(input("enter the number"))
    sub=n1-n2
    print(sub)
 sub()

 def mul():
    n1 = float(input("enter a number"))
    n2 = float(input("enter the number"))
    mul=n1*n2
    print(mul)
 mul()

 def div():
    n1 = float(input("enter a number"))
    n2 = float(input("enter the number"))
    div=n1//n2
    print(div)
 div()
select_operation()