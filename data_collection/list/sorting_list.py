my_list=[111,45,78,90,5,7,32,16]
sort=[]
while my_list:
    min=my_list[0]
    for i in my_list:
        if i<min:
            min=i
    sort.append(min)
    my_list.remove(min)

print(sort)



