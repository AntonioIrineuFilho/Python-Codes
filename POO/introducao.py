class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calcArea(self):
        area = self.b * self.h / 2
        return area

triangulo1 = Triangulo()
print(triangulo1)