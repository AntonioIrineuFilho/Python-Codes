from Bingo import Bingo

class UI:
    def proximo(jogo):
        print(f'Bola sorteada: {jogo.Proximo()}')
    def sorteados(jogo):
        print('Bolas sorteadas:', *jogo.Sorteados())
    def main():
        numBolas = int(input("Digite o número de bolas: "))
        jogo = Bingo(numBolas)
        run = True
        while (run):
            print("1-Próxima bola\n2-Bolas sorteadas\n3-Sair")
            op = int(input("Digite a opção desejada: "))
            match (op):
                case 1:
                    UI.proximo(jogo)
                case 2:
                    UI.sorteados(jogo)
                case 3:
                    print("FIM DE EXECUÇÃO.")
                    run = False

UI.main()