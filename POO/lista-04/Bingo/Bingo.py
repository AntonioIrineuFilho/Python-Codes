from random import randint

class Bingo:
    def __init__(self, numBolas):
        self.__bolas = []
        self.setNumBolas(numBolas)
    def setNumBolas(self, numBolas):
        if (numBolas <= 0):
            raise ValueError("INVALID VALUE")
        else:
            self.__numBolas = numBolas
    def Proximo(self):
        n = self.__numBolas
        if (len(self.__bolas) == n):
            return -1
        while True:
            x = randint(1, n)
            if (x not in self.__bolas):
                self.__bolas.append(x)
                return x
    def Sorteados(self):
        return self.__bolas