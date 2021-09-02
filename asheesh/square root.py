# num=float(input("enter the numer"))
# num_s=num**.5
# print('the sqareroot of %0.4f is %0.4f'%(num,num_s))
#




# for real and complex numbers

import cmath
num=float(input("enter the number"))
num_s=cmath.sqrt(num)
print('the square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num,num_s.real,num_s.imag))
