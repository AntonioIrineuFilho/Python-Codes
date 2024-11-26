from Item import Item

class Carrinho:
    def __init__(self, cliente, data, item):
        self.__itens = []
        self.setCliente(cliente)
        self.setData(data)
        self.Inserir(item)
    def setCliente(self, cliente):
        if (cliente == ""):
            raise ValueError("INVALID NAME")
        for i in range(len(cliente)):
            if (cliente[i] != " "):
                break
            if (i == len(cliente)-1):
                raise ValueError("INVALID CLIENT")
        self.__cliente = cliente.strip().upper()
    def setData(self, data):
        if (data == ""):
            raise ValueError("INVALID NAME")
        for i in range(len(data)):
            if (data[i] != " "):
                break
            if (i == len(data)-1):
                raise ValueError("INVALID CLIENT")
        self.__data = data.strip()
    def getCliente(self):
        return self.__cliente
    def getData(self):
        return self.__data
    def Inserir(self, item):
        self.__itens.append(item)
    def Remover(self, item):
        self.__itens.remove(item)
    def totalPreco(self):
        soma = 0
        for i in range(len(self.__itens)):
            soma += self.__itens[i].Total()
        return soma
    def totalQtd(self):
        soma = 0
        for i in range(len(self.__itens)):
            soma += self.__itens[i].getQuantidade()
        return soma
    def __str__(self):
        return f'Cliente: {self.__cliente}\nData: {self.__data}\nNúmero de itens: {self.totalQtd()}\nPreço total: R$ {self.totalPreco():.2f}'
    