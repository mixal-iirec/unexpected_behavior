import re

res = re.search('.', "\n")
print(res)
res = re.search('^(.*)$', "a\n")
print(res.groups())
