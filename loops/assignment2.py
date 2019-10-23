#WAP find the given numbern is prime number or not:

import math

n = int(input("enter the number: "))
if n == 2:
    print(True)

for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        print(False)
        break
else:
    print(True)



#-----------------------------------
''' 

def is_prime(n):
    #n = int(input("enter the number: "))
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) +1, 2):
        if n % i == 0:
            return False

    return True

p = is_prime(9)
print(p)

'''