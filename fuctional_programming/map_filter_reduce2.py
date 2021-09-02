lst=[2,3,4,5,6]
#squares of a list:map
#map
#map(fuction,list/itrable)

# square=lambda num:num**2
# print(list(square(lst)))
square=list(map(lambda num:num**2,lst))
print(square)

cubes=list(map(lambda num:num**3,lst))
print(cubes)

#print even numbers from list

#filter
#filter(fuction,iterable)
# def chk_even(num):
#     return  num%2==0
# evens=list(filter(chk_even,lst))
# print(evens)

evens=list(filter(lambda  num:num%2==0,lst))
print(evens)
odds=list(filter(lambda num:num%2!=0,lst))
print(odds)