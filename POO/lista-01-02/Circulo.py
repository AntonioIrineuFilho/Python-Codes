from math import pi

class Circulo:
    def __init__(self):
        self.raio = 0
    
    def Area(self):
        area = self.raio ** 2 * pi
        return area
    
    def Circunferencia(self):
        circunferencia = 2 * self.raio * pi
        return circunferencia

r = float(input("Digite o raio do círculo: "))
circulo1 = Circulo()
circulo1.raio = r
print(f'Área do círculo = {circulo1.Area():.1f}')
print(f'Circunferência do círculo = {circulo1.Circunferencia():.1f}')