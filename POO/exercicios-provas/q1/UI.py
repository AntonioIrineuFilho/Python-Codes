from Carrinho import Carrinho
from Item import Item
from random import randint

class UI:
    def main():
        listaItens = []
        for i in range(0, 5):
            produto = input("Digite o produto desejado: ")
            qtd = int(input("Digite a quantidade do produto: "))
            preco_unit = float(input("Digite o preço unitário: "))
            item = Item(produto, qtd, preco_unit)
            listaItens.append(item)
        cliente = input("Digite o seu nome: ")
        data = input("Digite a data da compra(dd/mm/aaaa): ")
        for i in range(len(listaItens)):
            if (i == 0):
                carrinho = Carrinho(cliente, data, listaItens[i])
            else:
                carrinho.Inserir(listaItens[i])
        x = randint(0, 4)
        carrinho.Remover(listaItens[x])
        print(carrinho)     


UI.main()