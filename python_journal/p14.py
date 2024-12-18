class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass
    def perimeter(self):
        pass
    def showName(self):
        return self.name

class Circle(Shape):
    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def area(self):
        return 3.14159 * self.r * self.r
    
    def perimeter(self):
        return 2 * 3.14159 * self.r
    

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
r = Rectangle('rect',4,3)
print(r.area())
print(r.perimeter())
print(r.showName())

c = Circle('circ',2.5)
print(c.area())
print(c.perimeter())
print(c.showName())
