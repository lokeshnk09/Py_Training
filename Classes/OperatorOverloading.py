class Product():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self, other):
        total=self.price+other.price
        self.price=total
        return self
    def __mul__(self, other):
        total=self.price*other.price
        self.price=total
        return self
ob1=Product('Coffee',23)
ob2=Product('Tea',12)
ob3=Product('Milk',10)
total=ob1+ob2+ob3
print(total.price)
totp=ob1*ob2*ob3
print(totp.price)