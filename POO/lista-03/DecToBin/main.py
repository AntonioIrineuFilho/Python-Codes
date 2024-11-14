from dectobin import DecToBin

class UI:
    def calcBin(valor):
        print(f'Número {valor.getNum()} em binário = {valor.Bin()}')
    def getValor(valor):
        print(valor)
    def setValor(valor):
        n = int(input("Digite o novo valor desejado: "))
        valor.setNum(n)
    def main():
        num = int(input("Digite um número inteiro: "))
        valor = DecToBin(num)
        run = True
        while (run):
            print("1-Calcular binário\n2-Ver valores\n3-Alterar valores\n4-Sair")
            op = int(input("Digite a opção desejada: "))
            while True:
                if (op < 1 or op > 4):
                    op = int(input("Opção inválida. Digite uma opção válida: "))
                else:
                    break
            match (op):
                case 1:
                    UI.calcBin(valor)
                case 2:
                    UI.getValor(valor)
                case 3:
                    UI.setValor(valor)
                case 4:
                    run = False

UI.main()