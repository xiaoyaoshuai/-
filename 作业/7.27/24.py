import re
phone = '17898737636'
ret = re.match('1\d{10}$',phone)
print(ret.group())

