from view import View

class UI:

    idClienteSessao = -1

    @staticmethod
    def menuVisitante():
        print(20*"-")
        print("MENU DO VISITANTE")
        print(20*"-")
        print("1-Cadastro no Sistema\n2-Entrar no Sistema")
        op = int(input("Digite a opção desejada: "))
        return op
    
    @staticmethod
    def menuAdmin():
        print(20*"-")
        print("MENU DO ADMIN")
        print(20*"-")
        print("1-Inserir Cliente\n2-Listar Clientes\n3-Atualizar Cliente\n4-Deletar Cliente\n")
        print("5-Inserir Categoria\n6-Listar Categorias\n7-Atualizar Categoria\n8-Deletar Categoria\n")
        print("9-Inserir Produto\n10-Listar Produtos\n11-Atualizar Produtos\n12-Deletar Produtos\n")
        print("13-Sair\n")
        op = int(input("Digite a opção desejada: "))
        return op
    
    @staticmethod 
    def menuCliente():
        print(20*"-")
        print("MENU DO CLIENTE")
        print(20*"-")
        print("1-Ver Categorias\n2-Ver Produtos\n3-Inserir Produto no Carrinho\n4-Ver Carrinho\n5-Atualizar Produto do Carrinho\n6-Remover Produto do Carrinho\n7-Finalizar Compra\n8-Sair")
        op = int(input("Digite a opção desejada: "))
        return op

    @classmethod
    def main(cls):
        View.criarAdmin()

        # MENU DO VISITANTE
        while (cls.idClienteSessao == -1):
            op = UI.menuVisitante()
            if (op == 1):
                UI.cadastrarVisitante()
            elif (op == 2):
                cls.idClienteSessao = UI.validarVisitante()
                if (cls.idClienteSessao == None):
                    cls.idClienteSessao = -1
            else:
                print("Opção inválida.")
        

        # MENU DO ADMIN
        if (cls.idClienteSessao == 0):
            run = True
            while(run):
                match(UI.menuAdmin()):
                    case 1: UI.inserirCliente()
                    case 2: UI.listarClientes()
                    case 3: UI.atualizarCliente()
                    case 4: UI.deletarCliente()
                    case 5: UI.inserirCategoria()
                    case 6: UI.listarCategorias()
                    case 7: UI.atualizarCategoria()
                    case 8: UI.deletarCategoria()
                    case 9: UI.inserirProduto()
                    case 10: UI.listarProdutos()
                    case 11: UI.atualizarProduto()
                    case 12: UI.deletarProduto()
                    case 13: run = False
                    case _: print("Opção inválida")
        
        # MENU DO CLIENTE
        else:
            run = True
            while(run):
                match(UI.menuCliente()):
                    case 1: UI.listarCategorias()
                    case 2: UI.listarProdutos()
                    case 3: UI.inserirNoCarrinho()
                    case 4: UI.verCarrinho()
                    case 5: UI.atualizarCarrinho()
                    case 6: UI.removerDoCarrinho()
                    case 7: UI.finalizarCompra()
                    case 8: run = False
                    case _: print("Opção inválida.")


 #-----------------VISITANTE-------------------------------------------------------------------------------------------------------------

    @classmethod
    def cadastrarVisitante(cls):
        desc = input("Digite seu nome: ")
        fone = input("Digite seu número de telefone: ")
        email = input("Digite seu e-mail: ")
        senha = input("Crie uma senha: ")
        View.inserirCliente(0, desc, fone, email, senha)

    @classmethod
    def validarVisitante(cls):
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")
        idCliente = View.validarVisitante(email, senha)
        if (idCliente == False):
            print("Cadastro não encontrado.")
            return None
        else:
            print(f"Bem-vindo, {View.nomeCliente(idCliente)}!")
            return idCliente

#-----------------ADMIN-------------------------------------------------------------------------------------------------------------        

    @classmethod
    def inserirCliente(cls):
        desc = input("Digite o nome do cliente: ")
        fone = input("Digite o número de telefone: ")
        email = input("Digite o e-mail do cliente: ")
        senha = input("Digite a senha do cliente: ")
        View.inserirCliente(0, desc, fone, email, senha)
    
    @classmethod
    def listarClientes(cls):
        clientes = View.listarClientes()
        if (len(clientes) == 0):
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(cliente)
    
    @classmethod
    def atualizarCliente(cls):
        clientes = View.listarClientes()
        if (len == clientes):
            print("Nenhum cliente cadastrado.")
            return
        id = int(input("Digite o ID do cliente que deseja atualizar: "))
        if not (View.validarClienteId(id)):
            print("Cliente não encontrado")
        else:
            desc = input("Digite o nome do cliente: ")
            fone = input("Digite o número de telefone: ")
            email = input("Digite o e-mail do cliente: ")
            senha = input("Digite a senha do cliente: ")
            View.atualizarCliente(id, desc, fone, email, senha)

    @classmethod
    def deletarCliente(cls):
        clientes = View.listarClientes()
        if (len == clientes):
            print("Nenhum cliente cadastrado.")
            return
        id = int(input("Digite o ID do cliente que deseja deletar: "))
        if not (View.validarClienteId(id)):
            print("Cliente não encontrado")     
        else:
            View.deletarCliente(id)

    @classmethod
    def inserirCategoria(cls):
        desc = input("Digite a descrição da categoria: ")
        View.inserirCategoria(0, desc)

    @classmethod
    def listarCategorias(cls):
        categorias = View.listarCategorias()
        if (len(categorias) == 0):
            print("Nenhuma categoria cadastrada.")
        else:
            for categoria in categorias:
                print(categoria)
    
    @classmethod
    def atualizarCategoria(cls):
        categorias = View.listarCategorias()
        if (len(categorias) == 0):
            print("Nenhuma categoria cadastrada.")
            return
        id = int(input("Digite o ID da categoria que deseja atualizar: "))
        if not (View.validarCategoriaId(id)):
            print("Categoria não encontrada.")
        else:
            desc = input("Digite a descrição da categoria: ")
            View.atualizarCategoria(id, desc)

    @classmethod
    def deletarCategoria(cls):
        categorias = View.listarCategorias()
        if (len(categorias) == 0):
            print("Nenhuma categoria cadastrada.")
            return
        id = int(input("Digite o ID da categoria que deseja deletar: "))
        if not (View.validarCategoriaId(id)):
            print("Categoria não encontrada.")
        else:
            View.deletarCategoria(id)
    
    @classmethod
    def inserirProduto(cls):
        desc = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade em estoque: "))
        idCategoria = int(input("Digite o ID da categoria do produto: "))
        View.inserirProduto(0, desc, preco, estoque, idCategoria)
    
    @classmethod
    def listarProdutos(cls):
        produtos = View.listarProdutos()
        if (len(produtos) == 0):
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(produto)
    
    @classmethod
    def atualizarProduto(cls):
        produtos = View.listarProdutos()
        if (len(produtos) == 0):
            print("Nenhum produto cadastrado.")
        id = int(input("Digite o ID do produto que deseja atualizar: "))
        if not (View.validarProdutoId(id)):
            print("Produto não encontrado.")
        else:
            desc = input("Digite a descrição do produto: ")
            preco = float(input("Digite o preço do produto: "))
            estoque = int(input("Digite a quantidade em estoque: "))
            idCategoria = int(input("Digite o ID da categoria do produto: "))
            View.atualizarProduto(id, desc, preco, estoque, idCategoria)
    
    @classmethod
    def deletarProduto(cls):
        produtos = View.listarProdutos()
        if (len(produtos) == 0):
            print("Nenhum produto cadastrado.")
        id = int(input("Digite o ID do produto que deseja deletar: "))
        if not (View.validarProdutoId(id)):
            print("Produto não encontrado.")
        else: 
            View.deletarProduto(id)

#-----------------CLIENTE-------------------------------------------------------------------------------------------------------------
    
    @classmethod
    def inserirNoCarrinho(cls):
        View.criarCarrinho(cls.idClienteSessao)
        idProduto = int(input("Digite o ID do produto desejado: "))
        qtd = int(input("Digite a quantidade do produto desejado: "))
        if (View.verificarEstoque(idProduto, qtd)):
            View.inserirNoCarrinho(idProduto, qtd, cls.idClienteSessao)
            View.salvarCarrinho()

    @classmethod
    def verCarrinho(cls):
        if not (View.verCarrinho(cls.idClienteSessao)):
            print("Carrinho vazio.")

    @classmethod
    def atualizarCarrinho(cls):
        if not (View.verificarCarrinho(cls.idClienteSessao)):
            print("Carrinho vazio.")
        else:
            idProduto = int(input("Digite o ID do produto que deseja atualizar no carrinho: "))
            qtd = int(input("Digite a nova quantidade desejada do produto: "))
            if (View.verificarEstoque(idProduto, qtd)):
                View.atualizarCarrinho(idProduto, qtd, cls.idClienteSessao)
                View.salvarCarrinho()
    
    @classmethod
    def removerDoCarrinho(cls):
        if not (View.verificarCarrinho(cls.idClienteSessao)):
            print("Carrinho vazio.")
        else:
            idProduto = int(input("Digite o ID do produto que deseja remover do carrinho: "))
            View.removerDoCarrinho(idProduto, cls.idClienteSessao)
            View.salvarCarrinho()

    @classmethod
    def finalizarCompra(cls):
        if not (View.verCarrinho(cls.idClienteSessao)):
            print("Carrinho vazio.")
        else:
           op = int(input("Digite 1 para confirmar a finalização do pedido ou qualquer número para continuar comprando: "))
           if (op == 1):
               View.finalizarCompra(cls.idClienteSessao)


UI.main()
        
