class Viagem:
    def __init__(self):
        dist = 0
        tempo = 0
    
    def Vm(self):
        return self.dist / self.tempo

viagem1 = Viagem()
viagem1.dist = float(input("Digite a distância(em KM): "))
viagem1.tempo = t = float(input("Digite a duração da viagem(em horas): "))
print(f'A velocidade média da viagem foi de {viagem1.Vm():.1f} km/h')
