import json
from models.Clientes import Clientes
from models.VendaItem import VendaItem

class Venda:
    def __init__(self, id, data, idCliente, itens):
        self.setId(id)
        self.setData(data)
        self.setTotal()
        self.setIdCliente(idCliente)
        self.__itens = itens
    def setId(self, id):
        if (id < 0):
            raise ValueError("INVALID ID")
        else:
            self.__id = id
    def setData(self, data):
        self.__data = data
    def setTotal(self):
        total = 0
        for obj in self.__itens:
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
    def getItens(self):
        return self.__itens
    def getId(self):
        return self.__id
    def getData(self):
        return self.__data
    def getTotal(self):
        return self.__total
    def getIdCliente(self):
        return self.__idCliente
    def __str__(self):
        return f'Id Carrinho: {self.getId()} Data: {self.getData()} Id Cliente: {self.getIdCliente()} Valor Total: R$ {self.getTotal():.2f}'
    def inserirItem(self, item):
        id = 0
        for obj in self.__itens:
            if (obj.getId() >= id):
                id = obj.getId()
        item.setId(id+1)
        self.itens.append(item)
    def listarItens(self):
        return self.__itens
    def atualizarItem(self, item):
        for obj in self.itens:
            if (obj.getId() == item.getId()):
                obj.setQuantidade(item.getQuantidade())
                return
        print("O item desejado não se encontra no carrinho.")
    def deletarItem(self, id):
        for obj in self.itens:
            if (obj.getId() == id):
                del(obj)
                return
        print("O item desejado não se encontra no carrinho.")

    

class Vendas:
    vendas = [] # guarda cada carrinho de cada cliente diferente

    @classmethod 
    def inserirVenda(cls, venda):
        cls.abrir()
        for obj in cls.vendas:
            if (obj.getId() == venda.getId()):
                return
        id = 0
        for obj in cls.vendas:
            if (obj.getId() >= id):
                id = obj.getId()
        venda.setId(id+1)
        cls.vendas.append(venda)
        cls.salvar()
    
    @classmethod
    def listarVendas(cls):
        cls.abrir()
        return cls.vendas
    
    @classmethod
    def atualizarVendas(cls, venda):
        cls.abrir()
        for obj in cls.vendas:
            if (obj.getId() == venda.getId()):
                obj.setData(venda.getData())
                cls.salvar()
                return
        print("Carrinho não encontrado.")
    
    @classmethod
    def deletarVendas(cls, id):
        cls.abrir()
        for obj in cls.vendas:
            if (obj.getId() == id):
                del(obj)
                cls.salvar()
                return
        print("Carrinho não encontrado.")

    @classmethod
    def abrir(cls):
        cls.vendas = []
        try:
            with open("vendas.json", mode = "r") as arquivo:
                vendas = json.load(arquivo)
            for obj in vendas:
                itens = [VendaItem(
                    i["_VendaItem__id"], 
                    i["_VendaItem__qtd"], 
                    i["_VendaItem__preco"], 
                    i["_VendaItem__idVenda"], 
                    i["_VendaItem__idProduto"]
                ) for i in obj["_Venda__itens"]]
                venda = Venda(obj["_Venda__id"], obj["_Venda__data"], obj["_Venda__idCliente"], itens)
                cls.vendas.append(venda)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
        
    @classmethod
    def salvar(cls):
        with open("vendas.json", mode= "w") as arquivo:
            json.dump(cls.vendas, arquivo, default=vars)
