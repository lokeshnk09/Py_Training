#WAP print mulitiplicaion table
n = int(input("enter N: "))
for i in range(1, 11):
    print(n,"*", i,"=",i*n)
else:
    print('No more updates')
print('Task over')


#WAP find the difference sqrs of sum of 1st N natureal numbers and sum of sqrs of 1st n natural numbers

#1**2 + 2**2 + 3**2 + 4**2 + ----- N**2) - (1+2+3+4+5+----n)**2
n = int(input('enter N: '))
sqr_sum = 0
sum_sqr = 0
for i in range(1, n+1):
    sqr_sum = sqr_sum + (i**2)
    sum_sqr += i
sum_sqr = sum_sqr**2
print('sqr_sum - sum-sqr=', sqr_sum - sum_sqr)