s1={1,2,3,4,5,6,7}
s2={5,6,7,8,9,10}
s3=set()
for i in s1:
    if i in s2:
        s3.add(i)
print(s3)