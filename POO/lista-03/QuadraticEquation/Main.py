from QuadraticEquation import QuadraticEquation

class UI:
    def CalcDelta(obj):
        print(f'Valor do delta = {obj.Delta():.2f}')
    def CalcRaiz1(obj):
        print(f'Valor da primeira raiz = {obj.Raiz1():.2f}')
    def CalcRaiz2(obj):
        print(f'Valor da segunda raiz = {obj.Raiz2():.2f}')
    def getValores(obj):
        print(obj)
    def setValores(obj):
        run = True
        while (run):
            print("1-Alterar A\n2-Alterar B\n3-Alterar C\n4-Sair")
            op = int(input("Digite a opção desejada: "))
            while True:
                if (op < 1 or op > 4):
                    op = int(input("Opção inválida. Digite uma opção válida: "))
                else:
                    break
            match (op):
                case 1:
                    a = float(input("Digite o novo valor de A: "))
                    obj.setNumA(a)
                case 2:
                    b = float(input("Digite o novo valor de B: "))
                    obj.setNumB(b)
                case 3:
                    c = float(input("Digite o novo valor de C: "))
                    obj.setNumC(c)
                case 4:
                    run = False

    def main():
        a = float(input("Digite o valor do coeficiente A: "))
        b = float(input("Digite o valor do coeficiente B: "))
        c = float(input("Digite o valor do coeficiente C: "))
        obj = QuadraticEquation(a, b, c)
        run = True
        while (run):
            print("1-Calcular delta\n2-Calcular raiz 1\n3-Calcular raiz 2\n4-Ver valores\n5-Alterar valores\n6-Sair")
            op = int(input("Digite a opção desejada: "))
            while True:
                if (op < 1 or op > 6):
                    op = int(input("Opção inválida. Digite uma opção válida: "))
                else:
                    break
            match (op):
                case 1:
                    UI.CalcDelta(obj)
                case 2:
                    UI.CalcRaiz1(obj)
                case 3:
                    UI.CalcRaiz2(obj)
                case 4:
                    UI.getValores(obj)
                case 5:
                    UI.setValores(obj)
                case 6:
                    print("FIM DE EXECUÇÃO.")
                    run = False

UI.main()