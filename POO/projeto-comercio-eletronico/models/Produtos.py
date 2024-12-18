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
        Categorias.abrir()
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
        return f'{self.getId()} - {self.getDescricao()} - R$ {self.getPreco():.2f} - {self.getEstoque()}(Estoque) - {self.getIdCategoria()}(Categoria)'
    
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
        produto.setIdCategoria(produto.getIdCategoria())
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
                break
            if (i == len(cls.produtos)-1):
                print("Produto não encontrado.")
                return
        cls.salvar()
    
    @classmethod
    def deletarProduto(cls, id):
        cls.abrir()
        for i in range(len(cls.produtos)):
            if (cls.produtos[i].getId() == id):
                del(cls.produtos[i])
                break
            if (i == len(cls.produtos)-1):
                print("Produto não encontrado.")
                return
        cls.salvar()

    @classmethod
    def abrir(cls):
        cls.produtos = []
        try:
            with open("json/produtos.json", mode="r") as arquivo:
                objetos = json.load(arquivo)
            for obj in objetos:
                p = Produto(obj["_Produto__id"], obj["_Produto__descricao"], obj["_Produto__preco"], obj["_Produto__estoque"], obj["_Produto__idCategoria"])
                cls.produtos.append(p)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    @classmethod
    def salvar(cls):
        with open("json/produtos.json", mode="w") as arquivo:
            json.dump(cls.produtos, arquivo, default=vars)

    
