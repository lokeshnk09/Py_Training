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
for r in range(1, row +1):
    for c in range(r):
        print("*",end=" ",)
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
for r in range(0, row):
    for c in range(r):
        print("*", end=" ", )
    print(" ")

# WAPto list all the natural numbers below 10 that are miltiples of 3 or 5,. The sum of

N = input("enter N: ")
sum = 0
for var in ragne(1, N):
    if (var % 3 == 0 or var % 5 == 0):
        print(var, end=" +")



'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''
N = int(input("enter No of fibonic elements"))
a = 1
b = 2
sum = 0

for num in range(N):
    print(a, end=" ")
    if(a % 2==0):
        sum = sum+a
    c = a+b
    a = b
    b = c
    print("\n sum of even fibo:", sum)