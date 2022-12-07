import math


class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def storoni(self):  
        sides = [self.side_1, self.side_2, self.side_3]
        for side in sides:
            if not isinstance(side, float, int):
                return False 
            if side <= 0:
                return False
        return sides[2] < sides[0] + sides[1]
        
    def perimeter(self):
        return round(self.side_1 + self.side_2 + self.side_3, 2)
    
    def square(self):
        per = self.perimeter() / 2
        return round((per * (per - self.side_1) * (per - self.side_2) * (per - self.side_3)) ** 0.5, 2)
    
trian = Triangle(4, 2, 2)
print(trian.perimeter())
print(trian.square())


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def proverka(self):
        if isinstance(self.radius, (int, float)):
            return self.radius > 0
        
    def fox(self):
        return round(2 * math.pi * self.radius, 2)

    def square(self):
        return round(math.pi * (self.radius ** 2), 2)

circ = Circle(3)
print(circ.radius)
print(circ.fox())
print(circ.square())