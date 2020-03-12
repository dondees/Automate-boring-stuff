import re

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
print(beginsWithHelloRegex.search('He said "Hello!"'))
print(beginsWithHelloRegex.search('He said "Hello!"'))

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))
print(endsWithWorldRegex.search('Hello world!dafdfadfadfa'))


allDigitsRegex = re.compile(r'^\d+$') # one or more digits
print(allDigitsRegex.search('243143143143144254464'))
print(allDigitsRegex.search('243143143x143144254464'))


atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))


## dot-star pattern .* - anything, any pattern 



