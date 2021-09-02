f1=open('file1copy','r')
f2 = open('newfilecopy', 'w')
for i in f1:
    f2.write(i)