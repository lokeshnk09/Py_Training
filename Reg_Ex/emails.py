
import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''


# pattern = re.compile(r'\d+[.|-]\d+[-|.]\d+')  # to get all Phone #'s'
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')  # to get all names
# to get all emails
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')


matches = pattern.finditer(emails)

for match in matches:
    print(match)
