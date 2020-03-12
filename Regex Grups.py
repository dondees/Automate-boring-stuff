import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
phoneNumRegex.search('My number is 415-555-4242')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group())


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
phoneNumRegex.search('My number is 415-555-4242')
phoneNumRegex.search('My number is (415) 555-4242')
mo.group()
print(mo.group())


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

mo = batRegex.search('Batmotorcycle lost a wheel')
mo == None
print(mo)
# print(mo.group()) None value doesn't have a method called group
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(1))