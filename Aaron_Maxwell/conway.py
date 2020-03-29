import random, time, copy

WIDTH = 5
HEIGHT = 5

# Create a list of list for the cells:

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)
