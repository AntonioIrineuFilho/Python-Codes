class Frete:
    def __init__(self, peso, dist):
        self.setPeso(peso)
        self.setDistancia(dist)
    def setPeso(self, peso):
        if (peso <= 0):
            raise ValueError("NEGATIVE OR NULL VALUE NOT ALLOWED")
        else:
            self.__peso = peso
    def getPeso(self):
        return self.__peso
    def setDistancia(self, dist):
        if (dist <= 0):
            raise ValueError("NEGATIVE OR NULL VALUE NOT ALLOWED")
        else:
            self.__dist = dist
    def getDistancia(self):
        return self.__dist
    def __str__(self):
        return f'Peso = {self.__peso:.2f} KG\nDistância = {self.__dist:.2f} KM'
    def CalcFrete(self):
        return self.__peso * self.__dist * 0.01