#stack
#lifo...last in first out
#push...add elements
#pop...remove elements
#display
#specify size
lst =[]
top=0
size=int(input("enter the size"))
n=0
def push():
    global top,size
    if(top>size):
        print("stack is full")
    else:
        ele=int(input("enter element want to push"))
        lst.append(ele)
        top+=1
def pop():
    global top,size
    if top<=0:
        print("stack is empty")
    else:
        lst.pop()
        top-=1
def display():
        print(lst)
while(n!=1):
    print("1.PUSH")
    print(("2.POP"))
    print("3.DISPLAY")
    choice=int(input("enter your choice"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    else:
       print("invalid operation")
    n=int(input("press 1 to exit!!press 2 to coninue"))

