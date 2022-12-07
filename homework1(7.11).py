from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetor(self):
        return round(self.a + self.b +self.c, 2) 
        

    def square(self):
        p = self.perimetor() /2
        return round(sqrt(p * (p - self.a ) * (p - self.b) * (p - self.c)), 2) 


t = Triangle(5, 5, 5)
print(t.perimetor())
print(t.square())


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def slonik(self):
        return round(2 * math.pi * self.radius, 2) 
    def square(self): 
        return round(math.pi * self.radius**2, 2) 

circ = Circle(4)
print(circ.slonik())
print(circ.square())