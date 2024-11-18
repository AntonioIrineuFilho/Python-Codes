from Data import Data

class UI:
    def verData(data):
        print(data)
    def verDia(data):
        print(f'Dia = {data.getDia()}')
    def verMes(data):
        print(f'Mês = {data.getMes()}')
    def verAno(data):
        print(f'Ano = {data.getAno()}')
    def setData(data):
        d = input("Digite a nova data(dd/mm/aaaa): ")
        data.setData(d)
    def main():
        d = input("Digite a data desejada(dd/mm/aaaa): ")
        data = Data(d)
        run = True
        while (run):
            print("1-Ver data completa\n2-Ver dia\n3-Ver mês\n4-Ver ano\n5-Alterar data\n6-Sair")
            op = int(input("Digite a opção desejada: "))
            while True:
                if (op < 1 or op > 6):
                    op = int(input("Opção inválida. Digite uma opção válida: "))
                else:
                    break
            match (op):
                case 1:
                    UI.verData(data)
                case 2:
                    UI.verDia(data)
                case 3:
                    UI.verMes(data)
                case 4:
                    UI.verAno(data)
                case 5:
                    UI.setData(data)
                case 6:
                    print("FIM DE EXECUÇÃO.")
                    run = False
UI.main()