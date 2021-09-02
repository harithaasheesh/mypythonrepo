lst=[2,3,4,6,8,9,76,56,44,32]
#print(len(lst))
def binarysrch():
    lst.sort()
    print(lst)
    numb=int(input("enter element"))
    flag=0
    low=0
    upp=len(lst)-1
    while low<=upp:
        mid=(low+upp)//2
        if numb>lst[mid]:
            low=mid+1
        elif numb<lst[mid]:
            upp=mid-1
        elif numb==lst[mid]:
            flag=1
            break
    if flag==1:
        print("found")
    else:
        print("not found")
binarysrch()
