a=[1,2,3,45,6,7,33,11,77,9,0,5]
b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
common=[]
for i in a:
    if i not in b:
        common.append(i)
    else:
        print(i)