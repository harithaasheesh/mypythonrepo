import re
x='\W'
matcher=re.finditer(x,'abSDFzx@#%Wc')
for match in matcher:
    print(match.start())
    print(match.group())