
def compute(n):
    result = []
    for i in range(2, n):
        while n % i == 0:
            n = n/i
            result.append(i)
        if n == 1:
            break
    if n > 1:
        result.append(n)
    print(result)


if __name__ == '__main__':
    compute(600851475143)

