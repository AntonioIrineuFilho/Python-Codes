from models.Clientes import Clientes
from models.VendasItens import VendasItens

class Venda:
    def __init__(self, id, data, idCliente):
        self.setId(id)
        self.setData(data)
        self.setCarrinho()
        self.setTotal()
        self.setIdCliente(idCliente)
    def setId(self, id):
        if (id < 0):
            raise ValueError("INVALID ID")
        else:
            self.__id = id
    def setData(self, data):
        self.__data = data
    def setCarrinho(self):
        if (len(VendasItens.listarItens()) > 0):
            self.__carrinho = True
        else:
            self.__carrinho = False
    def setTotal(self):
        total = 0
        for obj in VendasItens.listarItens():
            total += obj.getQuantidade() * obj.getPreco()
        self.__total = total
    def setIdCliente(self, idCliente):
        clientes = Clientes.clientes
        for i in range(len(clientes)):
            if (clientes[i].getId() == idCliente):
                self.__idCliente = idCliente
                break
            if (i == len(clientes)-1):
                raise ValueError("INVALID ID")
    def getId(self):
        return self.__id
    def getData(self):
        return self.__data
    def getCarrinho(self):
        return self.__carrinho
    def getTotal(self):
        return self.__total
    def getIdCliente(self):
        return self.__idCliente
    def __str__(self):
        return f'\n\033[1;33mNOTA FISCAL\n{self.getId()} - Data da Compra: {self.getData()} - Id do Cliente: {self.getIdCliente()} - Valor Total: R$ {self.getTotal():.2f}\033[m'
