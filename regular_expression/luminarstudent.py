import re
f2=open('python_student','w')
x='([L][U][M]\d{2}[P][Y]\d{3}$)'
f=open('luminar_student','r')
for i in f:
    number=i.rstrip("\n")
    matcher=re.fullmatch(x,number)
    if matcher!=None:
        f2.write(number)
        f2.write('\n')
