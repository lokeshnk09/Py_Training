class squaresIterator:
    def __init__(self, max_root):
        self.max_root = max_root
        self.current_root = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_root >= self.max_root:
            raise StopIteration
        square_root = self.current_root ** 2
        self.current_root += 1
        return square_root


for square in squaresIterator(9):
    print(square)