# import re
# x='[A-Z]'
# matcher=re.finditer(x,'abSDFzx@#%Wc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

import re
x='[a-zA-Z]'
matcher=re.finditer(x,'abSDFzx@#%Wc')
for match in matcher:
    print(match.start())
    print(match.group())