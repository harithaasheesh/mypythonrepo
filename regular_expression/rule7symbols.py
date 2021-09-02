import re
x='[^a-zA-Z0-9]'
matcher=re.finditer(x,'abSD Fzx@#%Wc')
for match in matcher:
    print(match.start())
    print(match.group())