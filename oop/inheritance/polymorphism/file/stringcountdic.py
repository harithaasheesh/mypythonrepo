dic={}
f1=open('stringcountdic','r')
for i in f1:
    b = i.split(" ")
    for i in b:
        if i not in dic:
            dic[i]=1
        else:
            val=int(dic[i])
            val=val+1
            dic.update({i:val})
print(dic)