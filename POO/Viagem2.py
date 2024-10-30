class Travel:
    def __init__(self, d, t):
        self.setDist(d)
        self.setTempo(t)
    def setDist(self, d):
        if (d >= 0):
            self.__d = d
        else:
            raise ValueError("distância negativa")
    def setTempo(self, t):
        if (t >= 0):
            self.__t = t
        else:
            raise ValueError("tempo negativo")
    def getDist(self):
        return self.__d
    def getTempo(self):
        return self.__t
    def velocidadeMedia(self):
        return self.__d / self.__t
    
class UI:
    def main():
        distancia = float(input("Digite a distância da viagem: "))
        tempo = float(input("Digite o tempo da viagem: "))
        