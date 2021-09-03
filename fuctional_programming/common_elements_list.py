lst=[10,11,12,20,21,30]
lst2=[20,21,22,23,24,30]
lst3=[]
# for i in lst:
#     if i not in lst2:
#         lst3.append(i)
#     else:
#         print(i)
pos1=0
pos2=0
if(lst[pos1]=lst2[pos2]):
    print(lst[pos1])
    pos1+=1
    pos2+=1
elif lst[pos1]<lst2[pos2]:
    pos1+=1
elif lst[pos1]>lst2[pos2]