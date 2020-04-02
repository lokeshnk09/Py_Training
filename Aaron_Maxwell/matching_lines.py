def matching_lines_from_lines(path, pattern):
    with open(path) as handle:
        for line in handle:
            if pattern in line:
                yield line.rstrip('\n')


for line in matching_lines_from_lines("C:\\Users\lnadimpalli\Documents\Book1.txt", '3782514'):
    print(line)