from models.Clientes import Cliente, Clientes
from models.Categorias import Categoria, Categorias
from models.Produtos import Produto, Produtos

class View:

    @staticmethod
    def validarClienteId(id):
        Clientes.abrir()
        clientes = Clientes.clientes
        for c in clientes:
            if (c.getId() == id):
                return True
        return False
    
    @staticmethod
    def validarCategoriaId(id):
        Categorias.abrir()
        categorias = Categorias.categorias
        for c in categorias:
            if (c.getId() == id):
                return True
        return False
    
    @staticmethod
    def validarProdutoId(id):
        Produtos.abrir()
        produtos = Produtos.produtos
        for p in produtos:
            if (p.getId() == id):
                return True
        return False
    
    @staticmethod
    def inserirCliente(id, nome, fone, email, senha):
        c = Cliente(id, nome, fone, email, senha)
        Clientes.inserirCliente(c)
    
    @staticmethod
    def listarClientes():
        return Clientes.listarClientes()
    
    @staticmethod
    def atualizarCliente(id, nome, fone, email, senha):
        c = Cliente(id, nome, fone, email, senha)
        Clientes.atualizarCliente(c)

    @staticmethod
    def deletarCliente(id):
        Clientes.deletarCliente(id)

    @staticmethod
    def inserirCategoria(id, desc):
        c = Categoria(id, desc)
        Categorias.inserirCategoria(c)
    
    @staticmethod
    def listarCategorias():
        return Categorias.listarCategorias()

    @staticmethod
    def atualizarCategoria(id, desc):
        c = Categoria(id, desc)
        Categorias.atualizarCategoria(c)

    @staticmethod
    def deletarCategoria(id):
        Categorias.deletarCategoria(id)

    @staticmethod
    def inserirProduto(id, desc, preco, estoque, idCategoria):
        p = Produto(id, desc, preco, estoque, idCategoria)
        Produtos.inserirProduto(p)
    
    @staticmethod
    def listarProdutos():
        return Produtos.listarProdutos()
    
    @staticmethod
    def atualizarProduto(id, desc, preco, estoque, idCategoria):
        p = Produto(id, desc, preco, estoque, idCategoria)
        Produtos.atualizarProduto(p)
    
    @staticmethod
    def deletarProduto(id):
        Produtos.deletarProduto(id)