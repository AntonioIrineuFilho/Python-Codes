class Retangulo:
    def __init__(self, base, altura):
        self.setBase(base)
        self.setAltura(altura)
    def setBase(self, base):
        if (base < 0):
            raise ValueError("NEGATIVE VALUE NOT ALLOWED")
        elif (base == 0):
            raise ValueError("NULL VALUE NOT ALLOWED")
        else:
            self.__base = base
    def getBase(self):
        return self.__base
    def setAltura(self, altura):
        if (altura < 0):
            raise ValueError("NEGATIVE VALUE NOT ALLOWED")
        elif (altura == 0):
            raise ValueError("NULL VALUE NOT ALLOWED")
        else:
            self.__altura = altura
    def getAltura(self):
        return self.__altura
    def CalcArea(self):
        return self.__base * self.__altura
    def CalcDiagonal(self):
        return (self.__base ** 2 + self.__altura ** 2) ** 0.5
    def __str__(self):
        return f'Base = {self.__base:.2f}\nAltura = {self.__altura:.2f}'
    