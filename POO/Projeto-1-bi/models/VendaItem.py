from models.Produtos import Produtos

class VendaItem:
    def __init__(self, id, qtd, preco, idVenda, idProduto):
        self.setId(id)
        self.setQuantidade(qtd)
        self.setPreco(preco)
        self.setIdVenda(idVenda)
        self.setIdProduto(idProduto)
    def setId(self, id):
        if (id < 0):
            raise ValueError("INVALID ID")
        else:
            self.__id = id
    def setQuantidade(self, qtd):
        if (qtd <= 0 ):
            raise ValueError("INVALID VALUE")
        else:
            self.__qtd = qtd
    def setPreco(self, preco):
        if (preco <= 0):
            raise ValueError("INVALID VALUE")
        else:
            self.__preco = preco
    def setIdVenda(self, idVenda):
            if (idVenda <= 0):
                print("INVALID ID")
            else:
                self.__idVenda = idVenda
    def setIdProduto(self, idProduto):
        produtos = Produtos.produtos
        for i in range(len(produtos)):
            if (produtos[i].getId() == idProduto):
                self.__idProduto = idProduto
            if (i == len(produtos)-1):
                raise ValueError("INVALID ID")
    def getId(self):
        return self.__id
    def getQuantidade(self):
        return self.__qtd
    def getPreco(self):
        return self.__preco
    def getIdVenda(self):
        return self.__idVenda
    def getIdProduto(self):
        return self.__idProduto
    def __str__(self):
        return f'Id: {self.getId()} Quantidade: {self.getQuantidade()} Preço Unitário: R$ {self.getPreco():.2f} Id Carrinho: {self.getIdVenda()} Id Produto: {self.getIdProduto()}'
    def converterEmDict(self):
        return {
            "id": self.getId(),
            "qtd": self.getQuantidade(),
            "preco": self.getPreco(),
            "idVenda": self.getIdVenda(),
            "idProduto": self.getIdProduto()
        }