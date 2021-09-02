import re
x='\d'
matcher=re.finditer(x,'abSD2zx@#36%Wc')
for match in matcher:
    print(match.start())
    print(match.group())