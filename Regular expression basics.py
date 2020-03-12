def isPhoneNumber(text): # 415-555-
    if len(text) != 12:
        return False # not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
        if text[7] != '-':
            return False # missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print(isPhoneNumber('5422342'))

message = 'Call me 515-666-77 tomorrow, or at 44-555-6666 for my office line'
foundNumber = False

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')



import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo = phoneNumRegex.search('Call me 515-666-777 tomorrow, or at 444-555-666 for my office line')
print(mo.group())

print(phoneNumRegex.findall('Call me 515-666-777 tomorrow, or at 444-555-666 for my office line'))