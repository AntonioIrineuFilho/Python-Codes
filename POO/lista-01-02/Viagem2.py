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
    def printGet(viagem):
        print(f'Distância = {viagem.getDist()}\nTempo = {viagem.getTempo()}')
    def set(viagem):
        distancia = float(input("Digite um novo valor para a distância: "))
        tempo = float(input("Digite um novo valor para o tempo: "))
        viagem.setDist(distancia)
        viagem.setTempo(tempo)
    def printVm(viagem):
        print(f'Velocidade média = {viagem.velocidadeMedia():.1f} km/h')
    def main():
        distancia = float(input("Digite a distância da viagem: "))
        tempo = float(input("Digite o tempo da viagem: "))
        viagem1 = Travel(distancia, tempo)
        ops = (1, 2, 3, 4)
        while True:
            print("1-Ver valores\n2-Alterar valores\n3-Calcular velocidade média\n4-Sair")
            op = int(input("Digite a opção desejada: "))
            while True:
                if (op in ops):
                    break
                else:
                    op = int(input("Opção inválida. Digite a opção desejada: "))
            if (op == 1):
                UI.printGet(viagem1)
            elif (op == 2):
                UI.set(viagem1)
            elif (op == 3):
                UI.printVm(viagem1)
            else:
                break

UI.main()

                

        