#wap find the prime numbers in b.w 20 to 40:
for num in range(20, 41):
    for var in range(2, num):
        if(num % var == 0):
            break
    else:
        print('Prime: ',num)



#WAP generate the fallowing pattern:
''' 
*
* *
* * *
* * * *
* * * * *
'''

row = 5
for r in range(0, row):
    for c in range(r):
        print("*", end=" ",)
    print(" ")

''' 
WAP 
*****
****
***
**
*
'''
row = 5
for r in range(1, row+1):
    for c in range(r, row +1):
        print("*", end=" ", )
    print(" ")




'''
   *
  ***
 *****
*******


'''
''' 
k = 0
rows = 10
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()
'''
''''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
N = int(input('Enter number: '))
for num in range(2, N+1):
    if(N % num ==0):
        for var in range(2, num):
            if(num % var == 0):
                break
        else:
            print(num)
