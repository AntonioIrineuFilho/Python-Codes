class Pessoa:
    def __init__(self, idade, altura):
        self.setIdade(idade)
        self.setAltura(altura)
    def setIdade(self, idade):
        if (idade >= 0):
            self.__idade = idade
        else:
            raise ValueError("idade negativa?")
    def setAltura(self, altura):
        if (altura >= 0):
            self.__altura = altura
        else:
            raise ValueError("altura negativa?")
    def __str__(self):
        return f'Idade: {self.__idade}\nAltura: {self.__altura}'
    # o método padrão str serve para printar uma string padrão quando o objeto por chamado sem método especificado
    # em java é toString

class UI:
    def main():
        idade = int(input("Digite sua idade: "))
        altura = float(input("Digite sua altura: "))
        pessoa1 = Pessoa(idade, altura)
        print(pessoa1)

UI.main()

