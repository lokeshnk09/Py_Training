def decorator_func(func):
    def wrapper_func(txt):
        print('x' * len(txt))
        func(txt)
        print('X' * len(txt))
    return wrapper_func


@decorator_func
def say_hello(txt):
    print(txt)


c = say_hello('Nirvaan Nadimpalli')

