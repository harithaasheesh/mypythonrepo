import re
x='[a-z]'
matcher=re.finditer(x,'abSDFzx@#%Wc')
for match in matcher:
    print(match.start())
    print(match.group())