#queue
#insertion...enqueue
#deletion.....dequeue
#first in first out...FIFO
queue=[]
size=int(input("enter the size"))
front=0
rear=0
n=0
def insertion():
    global size,front,rear,queue
    if rear>=size:
        print('queue is full')
    else:
        ele=int(input("enter the element want to insert"))
        queue.insert(rear,ele)
        #insert(position,element)
        rear+=1
        for i in range(front,rear):
            print(queue[i])
def deletion():
    global front,rear,size,queue
    if rear==front:
        print("queue is empty")
    else:
        front+=1
        for i in range(front,rear):
            print(queue[i])
while(n!=1):
    print("1.INSERTION")
    print("2.DELETION")
    choice=int(input("enter your choice"))
    if choice==1:
        insertion()
    elif choice==2:
        deletion()
    else:
        print("invalid operation")
        n=int(input("press 1 to exit!!press 2 to continue"))
