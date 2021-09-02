lst=[10,11,12,20,21,30]
lst2=[20,21,22,23,24,30]
lst3=[]
for i in lst:
    if i not in lst2:
        lst3.append(i)
    else:
        print(i)
