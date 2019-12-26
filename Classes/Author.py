class Author():
    def __init__(self,authorname,publishername):
        self.authorname=authorname
        print('Author init executes')
        super().__init__(publishername)
class Publisher():
    def __init__(self,publishername):
        self.publishername=publishername
        print('Publisher init executes')
class Book(Author,Publisher ):
    def __init__(self,name,price,authorname,publishername):
        self.name=name
        self.price=price
        super().__init__(authorname,publishername)
ob=Book('Python',500,'ABC','Wiley')
print('mro:',Book.mro())
'''print('Book Name',ob.name)
print('Book Price',ob.price)
print('Author Name',ob.authorname)
print('Publisher',ob.publishername)'''