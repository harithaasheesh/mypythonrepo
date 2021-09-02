import re
x='[0-9]'
matcher=re.finditer(x,'abS32DFz9x@#%Wc')
for match in matcher:
    print(match.start())
    print(match.group())