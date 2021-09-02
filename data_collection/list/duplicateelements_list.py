list=[2,3,4,5,5,6,2,9]
new=[]
for i in list:
    if i not in new:
        new.append(i)
    else:
       print(i)