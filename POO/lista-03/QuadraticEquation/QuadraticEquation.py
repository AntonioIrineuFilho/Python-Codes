class QuadraticEquation:
    def __init__(self, a, b, c):
        self.setNumA(a)
        self.setNumB(b)
        self.setNumC(c)
    def setNumA(self, a):
        self.__a = a
    def setNumB(self, b):
        self.__b = b
    def setNumC(self, c):
        self.__c = c
    def getNumA(self):
        return self.__a
    def getNumB(self):
        return self.__b
    def getNumC(self):
        return self.__c
    def __str__(self):
        return f'Coeficiente A = {self.__a:.2f}\nCoeficiente B = {self.__b:.2f}\nCoeficiente C = {self.__c:.2f}'
    def Delta(self):
        d = self.__b**2 - 4 * self.__a * self.__c
        return d
    def RaizesReais(self):
        delta = self.Delta()
        if (delta < 0):
            rr = False
        else:
            rr = True
        return rr
    def Raiz1(self):
        rr = self.RaizesReais()
        if not (rr):
            raise ValueError("NEGATIVE DELTA, NO REAL ROOTS")
        else:
            return (-self.__b + self.Delta()**0.5) / 2 * self.__a
    def Raiz2(self):
        rr = self.RaizesReais()
        if not (rr):
            raise ValueError("NEGATIVE DELTA, NO REAL ROOTS")
        else:
            return (-self.__b - self.Delta()**0.5) / 2 * self.__a
