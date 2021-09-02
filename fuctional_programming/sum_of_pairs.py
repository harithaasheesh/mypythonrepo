#lst=[2,4,6]=result[10,8,6]
lst=[2,4,6]
total=sum(lst)
# new_lst=[]
# for i in lst:
#     new_lst.append(total-i)
# print(new_lst)

print(list(map(lambda num:total-num,lst)))



#sum_of_pairs
# lst=[2,3,4,5]
# pair=6
# for i in lst:
#     for j in lst:
#         if(i!=j):
#             if(total==(i+j)):
#                 print(i,j)

#another method

# lst=[1,2,3,4,5]
# low=0
# upp=len(lst)-1
# pair=6
# pairs=[]
# while(low<upp):
#     sum=lst[low]+lst[upp]
#     if(sum==pair):
#         pairs.append((lst[low],lst[upp]))
#         low+=1
#     elif(sum>pair):
#         upp-=1
#     elif(sum<pair):
#         low+=1
# print(pairs)
