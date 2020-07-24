import os
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
lokeshnk.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''


sentence = 'Start a sentence and then bring it to an end'

# with open('emails.txt', 'r') as f:
#     contents = f.read()

# pattern = re.compile(r'\d+[.|-]\d+[-|.]\d+')  # to get all Phone #'s'
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')  # to get all names


matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
