s={1,2,3,4,5,6,67,55,78,22,11,34}
prime=set()
nonprime=set()
for i in s:
    if i>=1:
        for j in range(2,i):
            if(i%j)==0:
                nonprime.add(i)
                break
        else:
                prime.add(i)
print(prime)
print(nonprime)