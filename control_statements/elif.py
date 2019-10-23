#WAP find the salary based on exp:
exp = int(input("Enter no of years of exp:"))
if (exp >= 0 and exp < 2):
    print("3 lac PA")
elif(exp >= 2 and exp < 4):
    print('6 lac PA')
elif(exp >= 4 and exp < 6):
    print('8 lac PA')
elif(exp >= 6 and exp < 10):
    print('10 lac PA')
else:
    print("enter proper exp")


