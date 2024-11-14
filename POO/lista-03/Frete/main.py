from frete import Frete

class UI:
    def calcFrete(frete):
        print(f"Preço do frete = R$ {frete.CalcFrete():.2f}")
    def getValores(frete):
        print(frete)
    def setValores(frete):
        run = True
        while (run):
            print("1-Alterar peso\n2-Alterar distância\n3-Sair")
            op = int(input("Digite a opção desejada: "))
            while True:
                if (op < 1 or op > 3):
                    print("1-Alterar peso\n2-Alterar distância\n3-Sair")
                    op = int(input("Opção inválida. Digite uma opção válida: "))
                else:
                    break
            match (op):
                case 1:
                    peso = float(input("Digite o valor do novo peso: "))
                    frete.setPeso(peso)
                case 2:
                    dist = float(input("Digite o valor da nova distância: "))
                    frete.setDistancia(dist)
                case 3:
                    run = False
    def main():
        peso = float(input("Digite o peso da carga: "))
        dist = float(input("Digite a distância da viagem: "))
        frete1 = Frete(peso, dist)
        run = True
        while (run):
            print("1-Calcular frete\n2-Ver valores\n3-Alterar valores\n4-Sair")
            op = int(input("Digite a opção desejada: "))
            while True:
                if (op < 1 or op > 4):
                    print("1-Calcular frete\n2-Ver valores\n3-Alterar valores\n4-Sair")
                    op = int(input("Opção inválida. Digite uma opçaõ válida: "))
                else:
                    break
            match (op):
                case 1:
                    UI.calcFrete(frete1)
                case 2:
                    UI.getValores(frete1)
                case 3:
                    UI.setValores(frete1)
                case 4:
                    print("FIM DE EXECUÇÃO.")
                    run = False


UI.main()