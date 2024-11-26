class Item:
    def __init__(self, produto, qtd, preco_unit):
        self.setProduto(produto)
        self.setQuantidade(qtd)
        self.setPrecoUnit(preco_unit)
    def setProduto(self, produto):
        if (produto == ""):
            raise ValueError("INVALID PRODUCT NAME")
        for i in range(len(produto)):
            if (produto != " "):
                break
            if (i == len(produto)-1):
                raise ValueError("INVALID PRODUCT NAME")
        self.__produto = produto.strip().upper()
    def setQuantidade(self, qtd):
        if (qtd <= 0):
            raise ValueError("INVALID VALUE")
        self.__qtd = qtd
    def setPrecoUnit(self, preco_unit):
        if (preco_unit <= 0):
            raise ValueError("INVALID VALUE")
        self.__preco_unit = preco_unit
    def getProduto(self):
        return self.__produto
    def getQuantidade(self):
        return self.__qtd
    def getPrecoUnit(self):
        return self.__preco_unit
    def Total(self):
        return self.__qtd * self.__preco_unit
    def __str__(self):
        return f'Produto: {self.__produto}\nQuantidade: {self.__qtd}\nPreço Unitário: {self.__preco_unit:.2f}'
    