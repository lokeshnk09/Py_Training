import re


def decorator_func(func):
    def lookup(key, file):
        expression = {'Phones': r'\d+[.|-]\d+[-|.]\d+',
                      'Names': r'M(r|s|rs)\.?\s[A-Z]\w*'}
        for k, v in expression.items():
            if re.match(key, k):
                with open(file, 'r') as f:
                    contents = f.read()
                pattern = re.compile(v)
                matches = pattern.finditer(contents)
                for match in matches:
                    print(match)
        return func(key, file)
    return lookup


@decorator_func
def matched_pattern(key, file):
    print()


p = matched_pattern('Phones', 'Entries.txt')
n = matched_pattern('Names', 'Entries.txt')




