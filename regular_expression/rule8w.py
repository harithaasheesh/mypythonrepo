import re
x='\w'
matcher=re.finditer(x,'abSDFzx@#%Wc')
for match in matcher:
    print(match.start())
    print(match.group())