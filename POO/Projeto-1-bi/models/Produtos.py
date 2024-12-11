import json
from models.Categorias import Categoria, Categorias

class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.setId(id)
        self.setDescricao(descricao)
        self.setPreco(preco)
        self.setEstoque(estoque)
        self.setIdCategoria(idCategoria)
    def setId(self, id):
        if (id < 0):
            raise ValueError("INVALID ID")
        else:
            self.__id = id
    def setDescricao(self, descricao):
        if (descricao == ""):
            raise ValueError("INVALID DESCRIPTION")
        else:
            self.__descricao = descricao
    def setPreco(self, preco):
        if (preco <= 0):
            raise ValueError("INVALID PRICE")
        else:
            self.__preco = preco
    def setEstoque(self, estoque):
        if (estoque < 0):
            raise ValueError("INVALID VALUE")
        else:
            self.__estoque = estoque
    def setIdCategoria(self, idCategoria):
        for i in range(len(Categorias.categorias)):
            if (Categorias.categorias[i].getId() == idCategoria):
                self.__idCategoria = idCategoria
                break
            if (i == len(Categorias.categorias)-1):
                raise ValueError("CATEGORY NOT FOUND")
    def getId(self):
        return self.__id
    def getDescricao(self):
        return self.__descricao
    def getPreco(self):
        return self.__preco
    def getEstoque(self):
        return self.__estoque
    def getIdCategoria(self):
        return self.__idCategoria
    def __str__(self):
        return f'{self.getId()} - {self.getDescricao()} - {self.getPreco():.2f} - {self.getEstoque()} - {self.getIdCategoria()}(Categoria)'
    
class Produtos:
    produtos = []

    @classmethod
    def inserirProduto(cls, produto):
        cls.abrir()
        id = 0
        for obj in cls.produtos:
            if (obj.getId() > id):
                id = obj.getId()
        produto.setId(id+1)
        cls.produtos.append(produto)
        cls.salvar()
    
    @classmethod
    def listarProdutos(cls):
        cls.abrir()
        return cls.produtos
    
    @classmethod
    def atualizarProduto(cls, produto):
        cls.abrir()
        for i in range(len(cls.produtos)):
            if (cls.produtos[i].getId() == produto.getId()):
                cls.produtos[i].setDescricao(produto.getDescricao())
                cls.produtos[i].setPreco(produto.getPreco())
                cls.produtos[i].setEstoque(produto.getEstoque())
                cls.produtos[i].setIdCategoria(produto.getIdCategoria())
            if (i == len(cls.produtos)-1):
                return "Produto não encontrado."
        cls.salvar()
    
    @classmethod
    def deletarProduto(cls, id):
        cls.abrir()
        for i in range(len(cls.produtos)):
            if (cls.produtos[i].getId() == id):
                cls.produtos.remove(cls.produtos[i])
            if (i == len(cls.produtos)-1):
                return "Produto não encontrado."
        cls.salvar()

    @classmethod
    def abrir(cls):
        cls.produtos = []
        with open("produtos.json", mode="r") as arquivo:
            objetos = json.load(arquivo)
        for obj in objetos:
            p = Produto(obj["id"], obj["descricao"], obj["preco"], obj["estoque"], obj["idCategoria"])
            cls.produtos.append(p)

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump("produtos.json", arquivo, default=vars)

    
