#WAP find the biggest numbers from 3 numbers
a = input('enter a:')
b = input("enter b:")
c = input("enter c:")
if a < b:
    if a < c:
        big = a
    else:
        big = b
else:
    if b < c:
        big = c
    else:
        big = b

print("big=", b)

