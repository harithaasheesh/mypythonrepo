#keys are unique,values duplication allowed
#keys same type
#mutable
#keys homo,values hetro
#nesting possible
d={1:"hello",2:{1:2,4:3}}
print(d)


# dict={'name':'asheesh','age':10,'class':'first'}
# print(dict)
# print(type(dict))
# print(dict['name'])
# print("dict['age']:",dict['age'])

#empty dictionary
# dic={}
# print(dic)
# print(type(dic))

#update existing entry
dict={'name':'asheesh','age':10,'class':'first'}
dict['age']=11
print(dict)

#add new entrty
dict1={'name':'asheesh','age':10,'class':'first'}
dict1['school']='ss school'
print(dict1)
#or
dict1.update({'location':'kochi'})
print(dict1)

#remove

# del dict1['school']
# print(dict1)
# dict1.clear()
# print(dict1)
# del dict1
# print(dict1)