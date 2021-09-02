import re
x='[^abc]'
matcher=re.finditer(x,'abdfcthjcd')
for match in matcher:
    print(match.start())
    print(match.group())

