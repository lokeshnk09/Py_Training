
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?



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

