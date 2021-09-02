#pattern matching
#re-(regul expresion)...package for pattern martching

# import re
# count=0
# matcher=re.finditer('ab','ababbbababababa')
# for match in matcher:
#     count=count+1
# print("count=",count)


import re
count=0
matcher=re.finditer('ab','ababbbababababa')
for match in matcher:
    print("match available at",match.start())  #return position
    print("group",match.group())     #which object find match
    count=count+1
print("count=",count)