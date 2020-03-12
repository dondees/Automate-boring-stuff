import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# powyzsze zwraca list of strings jezeli nie mamy zadnych nawiasow w telefonie

# wczytuje resume ctrc ctrl v resume = '.....'
# chce znalezc wszystkie nr telefonow

phoneRegex.search(resume)
phoneRegex.findall(resume)
# zwraca listy 

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneRegex.findall(resume)
# powyzsze zwroci stringi w listach poniewaz sa grupy
# po dwa stringi w dwoch listach

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
phoneRegex.findall(resume)
# teraz beda trzy stringi, po trzy stringi w dwoch listach

# \d - character class

digitRegex = re.compile(r'(0|1|2|3|4|5|6|7|8|9')
# represent any numeric digit from 0 to 9 robi to samo co
# digitRegex = re.compile(r'\d)
# table 7-1 dla innych character common character classes


lyrics ='12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming, 6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, 2 Turtle Doves, and 1 Partridge in a Pear Tree'

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall(lyrics)


vowelRegex = re.compile(r'[aeiouAEIOU]') # same as r'(a|e|i|o|u)'
vowelRegex = re.compile(r'[a-z]')

vowelRegex.findall('Robocop eats baby food')

vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
vowelRegex.findall('Robocop eats baby food')


# negative (every character that isn't specified)

consonantsRegex = re.compile(r'[^aeiouAEIOU]') # same as r'(a|e|i|o|u)'
consonantsRegex.findall('Robocop eats baby food')
