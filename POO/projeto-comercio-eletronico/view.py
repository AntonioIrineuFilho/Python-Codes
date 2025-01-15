from models.Clientes import Cliente, Clientes
from models.Categorias import Categoria, Categorias
from models.Produtos import Produto, Produtos
from models.VendasItens import VendaItem, VendasItens
from models.Venda import Venda
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
        return -1

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
    def NotaFiscal(idClienteSessao):
        return Venda(1, date.today(), idClienteSessao)

    @staticmethod
    def verificarEstoque(id, qtd):
        p = Produtos.listarProdutos()
        for obj in p:
            if (obj.getId() == id):
                if (obj.getEstoque() >= qtd):
                    return "ok"
                else:
                    return "\n\033[1;31mEstoque insuficiente.\033[m"
        return "\n\033[1;31mO produto do ID digitado não consta no carrinho.\033[m"
    
    @staticmethod
    def verificarCarrinho(idClienteSessao):
        venda = View.NotaFiscal(idClienteSessao)
        return venda.getCarrinho()
    
    @staticmethod
    def inserirNoCarrinho(idProduto, qtd):
        produtos = Produtos.listarProdutos()
        for p in produtos:
            if (p.getId() == idProduto):
                preco = p.getPreco()
                break
        v = VendaItem(0, qtd, preco, 1, idProduto)
        VendasItens.inserirItem(v)
    
    @staticmethod
    def verCarrinho(idClienteSessao):
        venda = View.NotaFiscal(idClienteSessao)
        if not (venda.getCarrinho()):
            return None
        else:
            return VendasItens.listarItens()
    
    @staticmethod
    def atualizarCarrinho(idProduto, qtd):
        carrinho = VendasItens.listarItens()
        for i in carrinho:
            if (i.getIdProduto() == idProduto):
                idItem = i.getId()
                preco = i.getPreco()
                break
        v = VendaItem(idItem, qtd, preco, 1, idProduto)
        VendasItens.atualizarItem(v)
        return True

    @staticmethod
    def removerDoCarrinho(idProduto):
        carrinho = VendasItens.listarItens()
        for i in carrinho:
            if (i.getIdProduto() == idProduto):
                VendasItens.deletarItem(i.getId())
                return True
        return False
        
    @staticmethod
    def finalizarCompra(idClienteSessao):
        venda = View.NotaFiscal(idClienteSessao)
        carrinho = VendasItens.listarItens()
        produtos = Produtos.listarProdutos()
        for item in carrinho:
            idProduto = item.getIdProduto()
            qtdCompra = item.getQuantidade()
            for p in produtos:
                if (p.getId() == idProduto):
                    estoqueAtualizado = p.getEstoque()-qtdCompra
                    produto = Produto(p.getId(), p.getDescricao(), p.getPreco(), estoqueAtualizado, p.getIdCategoria())
                    Produtos.atualizarProduto(produto)
                    break
        return venda
                