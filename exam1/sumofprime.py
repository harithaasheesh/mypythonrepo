def prime(max):
    s=0
    for i in range(1,max+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
               s=s+i
    return s
    # print("sum of prime numbers=",s)
print("sum=",prime(50))

