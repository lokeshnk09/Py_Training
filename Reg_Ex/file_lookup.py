import re


def lookup(key, file):
    expression = {'Phones': r'\d+[.|-]\d+[-|.]\d+',
                  'Names': r'M(r|s|rs)\.?\s[A-Z]\w*'}
    # d = {k: v for k, v in expression.items()}
    for k, v in expression.items():
        if re.match(key, k):
            with open(file, 'r') as f:
                contents = f.read()
            pattern = re.compile(v)
            matches = pattern.finditer(contents)
            for match in matches:
                print(match)



c = lookup('Names', 'Entries.txt')



