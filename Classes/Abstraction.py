from abc import ABC,abstractmethod


class Shape(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    def show(self):
        print('Color of Shape is',self.color)


class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        super().__init__(color)

    def perimeter(self):
        per = 4 * self.side
        print('Perimeter of Square:', per)


class Circle(Shape):
    def __init__(self,radius,color):
        self.radius=radius
        super().__init__(color)

    def perimeter(self):
        per = 2*3.14* self.radius
        print('Perimeter of Cericle:',per)


ob = Circle(3, 'Red')
ob.perimeter()
ob.show()