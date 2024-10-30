class Triangulo:
    def __init__(self, b, h):
        self.setBase(b)
        self.setAltura(h)
    def setBase(self, b):
        if (b >= 0):
            self.__base = b
        else:
            raise ValueError("a base não pode ser negativa")
    def setAltura(self, h):
        if (h >= 0):
            self.__altura = h
        else:
            raise ValueError("a altura não pode ser negativa")
    def getBase(self):
        return self.__base
    def getAltura(self):
        return self.__altura
    def calcArea(self):
        return self.__base * self.__altura / 2
        
class UI:
    def main():
        b = float(input("Digite a base do triângulo: "))
        h = float(input("Digite a altura do triângulo: "))
        t1 = Triangulo(b, h)
        print(f'A área do triângulo é {t1.calcArea():.1f}')
    def menu():
        run = True
        while run:
            print("1-Calcular área\n2-Sair")
            op = int(input("Digite a opção desejada: "))
            while True:
                if (op == 1 or op == 2):
                    break
                else:
                    op = int(input("Opção inválida. Digite a opção desejada: "))
            if (op == 1):
                UI.main()
            else:
                run = False
        
UI.menu()