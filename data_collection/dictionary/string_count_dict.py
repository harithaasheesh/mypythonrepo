a=input("enter")
b=a.split(" ")
count_dic={}
for i in b:
    if i not in  count_dic:
        count_dic[i]=1
        #count_dic.update({i:1})
    else:
        val=int(count_dic[i])
        val=val+1
        count_dic.update({i:val})
print(count_dic)