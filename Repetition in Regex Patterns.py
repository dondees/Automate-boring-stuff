import re

batRegex = re.compile(r'Bat(wo)?man') # appear 0 or 1 times
mo = batRegex.search('The Adventure of Batman')
print(mo.group())

mo = batRegex.search('The adventure of Batwoman')
print(mo.group())

mo = batRegex.search('The Adventure of Batwowowoman')
mo == None
print(mo)

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow')
print(mo.group())

mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow')
mo == None
print(mo)

phoneRegex = re.compile(r'(\d\d\d)?-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow')
print(mo.group())


# * - match zero or more times

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventure of Batman')
print(mo.group())
mo = batRegex.search('The Adventure of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventure of Batwowowowoman')
print(mo.group())


# + - match one or more times, must appear at least once, it's not optional
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventure of Batman') == None
print(mo)
mo = batRegex.search('The Adventure of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventure of Batwowowowoman')
print(mo.group())


# Escaping ?, *, +
regex = re.compile(r'\+\*\?')
mo = regex.search(' I learned about +*? regex syntax')
print(mo)
regex = re.compile(r'(\+\*\?)+') #match one or more in ()
mo = regex.search(' I learned about +*?+*?+*?+*?+*?+*?+*? regex syntax')
print(mo)


# x - exactly x
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo)
print(mo.group())

haRegex = re.compile(r'HaHaHa') # same as above
mo = haRegex.search('He said "HaHaHa"')
print(mo)
print(mo.group())

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234, 555-4242, 212-555-0000')
print(mo)

# x,y - at least x, at most y
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said "HaHaHa"')
print(mo)

mo = haRegex.search('He said "HaHaHaHa"')
print(mo)

mo = haRegex.search('He said "HaHaHaHaHaHaHaHa"')
print(mo)

# haRegex = re.compile(r'(Ha){3,}')

digitRegex = re.compile(r'\d{3,5}')
mo = digitRegex.search('1234567890')
print(mo)

digitRegex = re.compile(r'\d{3,5}?') # non-greedy match, match the smallest

mo = digitRegex.search('1234567890')
print(mo)