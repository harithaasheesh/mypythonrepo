#1..keeping order
#2.S..SUPPORT DUPLICATION
#3..heterogeneaus
# list=[1,2,3,4,5,0,1,4.5,True,"hello"]
# print(list)
# print(type(list))
# for i in list:
#     print(i)

#empty list
# list1=[]
# print(list1)
# list1.append(8)
# list1.append("hai")
# list1.append("4.6")
# print(list1)

#nesting possible

l=[1,2,3,[4,5,[6,7,8,9]]]
print(l)
l.remove(3)
print(l)      #list is mutable...update elements
l.clear()
print(l)
del l       #nesting possible
print(l)