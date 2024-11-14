from retangulo import Retangulo

class UI:
    def calcArea(retangulo):
        print(f'Área = {retangulo.CalcArea():.2f}')
    def calcDiagonal(retangulo):
        print(f'Diagonal = {retangulo.CalcDiagonal():.2f}')
    def getValores(retangulo):
        print(retangulo)
    def setValores(retangulo):
        while True:
            print("1-Alterar base\n2-Alterar altura\n3-Sair")
            op = int(input("Digite a opção desejada: "))
            while True:
                if (op == 1 or op == 2 or op == 3):
                    break
                else:
                    op = int(input("Opção inválida. Digite uma opção válida: "))
            if (op == 1):
                base = float(input("Digite o novo valor da base: "))
                retangulo.setBase(base)
            elif (op == 2):
                altura = float(input("Digite o novo valor da altura: "))
                retangulo.setAltura(altura)
            else:
                break
    def main():
        base = float(input("Digite o valor da base: "))
        altura = float(input("Digite o valor da altura: "))
        retangulo1 = Retangulo(base, altura)
        while True:
            print("1-Calcular área\n2-Calcular diagonal\n3-Ver valores\n4-Alterar valores\n5-Sair")
            op = int(input("Digite a opção desejada: "))
            while True:
                if (op < 1 or op > 5):
                    op = int(input("Opção inválida. Digite uma opção válida: "))
                else:
                    break
            if (op == 1):
                UI.calcArea(retangulo1)
            elif (op == 2):
                UI.calcDiagonal(retangulo1)
            elif (op == 3):
                UI.getValores(retangulo1)
            elif (op == 4):
                UI.setValores(retangulo1)
            else:
                print("FIM DE EXECUÇÂO.")
                break

UI.main()