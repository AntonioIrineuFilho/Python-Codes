from models.Clientes import Cliente, Clientes
from models.Categorias import Categoria, Categorias
from models.Produtos import Produto, Produtos
from models.VendaItem import VendaItem
from models.Vendas import Venda, Vendas
from datetime import date

class View:

    @staticmethod
    def criarAdmin():
        clientes = Clientes.listarClientes()
        c = Cliente(0, "Admin", "0000-0000", "admin", "admin")
        for obj in clientes:
            if (obj.getEmail() == c.getEmail() and obj.getSenha() == c.getSenha()):
                return
        Clientes.inserirCliente(c)

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
    def validarVisitante(email, senha):
        clientes = Clientes.listarClientes()
        for c in clientes:
            if (c.getEmail() == email and c.getSenha() == senha):
                return c.getId()
        return False

    @staticmethod
    def nomeVisitante(id):
        clientes = Clientes.listarClientes()
        for c in clientes:
            if (c.getId() == id):
                return c.getNome()

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

    @staticmethod
    def criarCarrinho(idClienteSessao):
        v = Venda(0, date.today(), idClienteSessao)
        Vendas.inserirVenda(v)
    
    @staticmethod
    def verificarCarrinho(idClienteSessao):
        carrinhos = Vendas.listarVendas()
        for c in carrinhos:
            if (c.getIdCliente() == idClienteSessao):
                return True
        return False

    @staticmethod
    def verificarEstoque(id, qtd):
        p = Produtos.listarProdutos()
        for obj in p:
            if (obj.getId() == id):
                if (obj.getEstoque() >= qtd):
                    return True
                else:
                    print("Estoque insuficiente.")
                    return False
        print("ID do produto inválido.")
        return False

    
    @staticmethod
    def inserirNoCarrinho(idProduto, qtd, idClienteSessao):
        carrinhos = Vendas.listarVendas()
        produtos = Produtos.listarProdutos()
        for c in carrinhos:
            if (c.getIdCliente() == idClienteSessao):
                for p in produtos:
                    if (p.getId() == idProduto):
                        preco = p.getPreco()
                        break
                v = VendaItem(0, qtd, preco, c.getId(), idProduto)
                c.inserirItem(v)
    
    @staticmethod
    def verCarrinho(idClienteSessao):
        carrinhos = Vendas.listarVendas()
        for c in carrinhos:
            if (c.getIdCliente() == idClienteSessao):
                print(c)
                return
        return False
    
    @staticmethod
    def atualizarCarrinho(idProduto, qtd, idClienteSessao):
        carrinhos = Vendas.listarVendas()
        produtos = Produtos.listarProdutos()
        for c in carrinhos:
            if (c.getIdCliente() == idClienteSessao):
                itens = c.getItens()
                for i in itens:
                    if (i.getIdProduto() == idProduto):
                        idItem = i.getId()
                for p in produtos:
                    if (p.getId() == idProduto):
                        preco = p.getPreco()
                        break
                v = VendaItem(idItem, qtd, preco, c.getId(), idProduto)
                c.atualizarItem(v)
                return True
            

    @staticmethod
    def removerDoCarrinho(idProduto, idClienteSessao):
        carrinhos = Vendas.listarVendas()
        for c in carrinhos:
            if (c.getIdCliente() == idClienteSessao):
                itens = c.getItens()
                for i in itens:
                    if (i.getIdProduto() == idProduto):
                        idItem = i.getId()
                c.deletarItem(idItem)