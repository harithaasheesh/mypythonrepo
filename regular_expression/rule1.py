import re
x='[abc]'
matcher=re.finditer(x,'ab dfdc')
for match in matcher:
    print(match.start())
    print(match.group())