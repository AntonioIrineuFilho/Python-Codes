from view import View

class UI:

    idClienteSessao = -1

    @staticmethod
    def menuVisitante():
        print(25*"\033[1;36m-\033[m")
        print("    \033[1;36mMENU DO VISITANTE\033[m")
        print(25*"\033[1;36m-\033[m")
        print("1-Cadastro no Sistema\n2-Entrar no Sistema")
        op = int(input("\nDigite a opção desejada: "))
        return op
    
    @staticmethod
    def menuAdmin():
        print(25*"\033[1;36m-\033[m")
        print("      \033[1;36mMENU DO ADMIN\033[m")
        print(25*"\033[1;36m-\033[m")
        print("1-Inserir Cliente\n2-Listar Clientes\n3-Atualizar Cliente\n4-Deletar Cliente")
        print(25*"-")
        print("5-Inserir Categoria\n6-Listar Categorias\n7-Atualizar Categoria\n8-Deletar Categoria")
        print(25*"-")
        print("9-Inserir Produto\n10-Listar Produtos\n11-Atualizar Produto\n12-Deletar Produto")
        print(25*"-")
        print("13-Sair\n")
        op = int(input("Digite a opção desejada: "))
        return op
    
    @staticmethod 
    def menuCliente():
        print(25*"\033[1;36m-\033[m")
        print("     \033[1;36mMENU DO CLIENTE\033[m")
        print(25*"\033[1;36m-\033[m")
        print("1-Ver Categorias\n2-Ver Produtos\n3-Inserir Produto no Carrinho\n4-Ver Carrinho\n5-Atualizar Produto do Carrinho\n6-Remover Produto do Carrinho\n7-Finalizar Compra\n8-Sair")
        op = int(input("\nDigite a opção desejada: "))
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
            else:
                print("\n\033[1;31mOpção inválida.\033[m")
        

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
                    case 13: 
                        print("\n\033[1;37mFIM DE EXECUÇÃO.\033[m")
                        run = False
                    case _: print("\n\033[1;31mOpção inválida.\033[m")
        
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
                    case 8: 
                        print("\n\033[1;37mFIM DE EXECUÇÃO.\033[m")
                        run = False
                    case _: print("\n\033[1;31mOpção inválida.\033[m")


 #-----------------VISITANTE-------------------------------------------------------------------------------------------------------------

    @classmethod
    def cadastrarVisitante(cls):
        desc = input("Digite seu nome: ")
        fone = input("Digite seu número de telefone: ")
        email = input("Digite seu e-mail: ")
        senha = input("Crie uma senha: ")
        View.inserirCliente(0, desc, fone, email, senha)
        print("\n\033[1;32mCliente cadastrado! Por favor, entre no sistema para ter acesso ao programa.\033[m")

    @classmethod
    def validarVisitante(cls):
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")
        idCliente = View.validarVisitante(email, senha)
        if (idCliente < 0):
            print("\n\033[1;31mE-mail ou senha inválidos.\033[m")
            return idCliente
        else:
            print(f"\nBem-vindo, \033[1;35m{View.nomeVisitante(idCliente).upper()}\033[m!")
            return idCliente

#-----------------ADMIN-------------------------------------------------------------------------------------------------------------        

    @classmethod
    def inserirCliente(cls):
        desc = input("Digite o nome do cliente: ")
        fone = input("Digite o número de telefone: ")
        email = input("Digite o e-mail do cliente: ")
        senha = input("Digite a senha do cliente: ")
        View.inserirCliente(0, desc, fone, email, senha)
        print("\n\033[1;32mCliente inserido!\033[m")
    
    @classmethod
    def listarClientes(cls):
        clientes = View.listarClientes()
        if (len(clientes) == 0):
            print("\nNenhum cliente cadastrado.")
        else:
            print(25*"-")
            for cliente in clientes:
                print(cliente)
    
    @classmethod
    def atualizarCliente(cls):
        clientes = View.listarClientes()
        if (len == clientes):
            print("\nNenhum cliente cadastrado.")
            return
        id = int(input("Digite o ID do cliente que deseja atualizar: "))
        if not (View.validarClienteId(id)):
            print("\n\033[1;31mCliente não encontrado.\033[m")
        else:
            desc = input("Digite o nome do cliente: ")
            fone = input("Digite o número de telefone: ")
            email = input("Digite o e-mail do cliente: ")
            senha = input("Digite a senha do cliente: ")
            View.atualizarCliente(id, desc, fone, email, senha)
            print("\n\033[1;32mCliente atualizado!\033[m")

    @classmethod
    def deletarCliente(cls):
        clientes = View.listarClientes()
        if (len == clientes):
            print("Nenhum cliente cadastrado.")
            return
        id = int(input("Digite o ID do cliente que deseja deletar: "))
        if not (View.validarClienteId(id)):
            print("\033[1;31mCliente não encontrado.\033[m")     
        else:
            View.deletarCliente(id)
            print("\n\033[1;32mCliente deletado!\033[m")

    @classmethod
    def inserirCategoria(cls):
        desc = input("Digite a descrição da categoria: ")
        View.inserirCategoria(0, desc)
        print("\n\033[1;32mCategoria inserida!\033[m")

    @classmethod
    def listarCategorias(cls):
        categorias = View.listarCategorias()
        if (len(categorias) == 0):
            print("\nNenhuma categoria cadastrada.")
        else:
            print(25*"-")
            for categoria in categorias:
                print(categoria)
    
    @classmethod
    def atualizarCategoria(cls):
        categorias = View.listarCategorias()
        if (len(categorias) == 0):
            print("\nNenhuma categoria cadastrada.")
            return
        id = int(input("Digite o ID da categoria que deseja atualizar: "))
        if not (View.validarCategoriaId(id)):
            print("\n\033[1;31mCategoria não encontrada.\033[m")
        else:
            desc = input("Digite a descrição da categoria: ")
            View.atualizarCategoria(id, desc)
            print("\n\033[1;32mCategoria atualizada!\033[m")

    @classmethod
    def deletarCategoria(cls):
        categorias = View.listarCategorias()
        if (len(categorias) == 0):
            print("\nNenhuma categoria cadastrada.")
            return
        id = int(input("Digite o ID da categoria que deseja deletar: "))
        if not (View.validarCategoriaId(id)):
            print("\n\033[1;31mCategoria não encontrada.\033[m")
        else:
            View.deletarCategoria(id)
            print("\n\033[1;32mCategoria deletada!\033[m")
    
    @classmethod
    def inserirProduto(cls):
        desc = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade em estoque: "))
        idCategoria = int(input("Digite o ID da categoria do produto: "))
        View.inserirProduto(0, desc, preco, estoque, idCategoria)
        print("\n\033[1;32mProduto inserido!\033[m")
    
    @classmethod
    def listarProdutos(cls):
        produtos = View.listarProdutos()
        if (len(produtos) == 0):
            print("\nNenhum produto cadastrado.")
        else:
            print(25*"-")
            for produto in produtos:
                print(produto)
    
    @classmethod
    def atualizarProduto(cls):
        produtos = View.listarProdutos()
        if (len(produtos) == 0):
            print("\nNenhum produto cadastrado.")
        id = int(input("Digite o ID do produto que deseja atualizar: "))
        if not (View.validarProdutoId(id)):
            print("\n\033[1;31mProduto não encontrado.\033[m")
        else:
            desc = input("Digite a descrição do produto: ")
            preco = float(input("Digite o preço do produto: "))
            estoque = int(input("Digite a quantidade em estoque: "))
            idCategoria = int(input("Digite o ID da categoria do produto: "))
            View.atualizarProduto(id, desc, preco, estoque, idCategoria)
            print("\n\033[1;32mProduto atualizado!\033[m")
    
    @classmethod
    def deletarProduto(cls):
        produtos = View.listarProdutos()
        if (len(produtos) == 0):
            print("\nNenhum produto cadastrado.")
        id = int(input("Digite o ID do produto que deseja deletar: "))
        if not (View.validarProdutoId(id)):
            print("\n\033[1;31mProduto não encontrado.\033[m")
        else: 
            View.deletarProduto(id)
            print("\n\033[1;32mProduto deletado!\033[m")

#-----------------CLIENTE-------------------------------------------------------------------------------------------------------------
    
    @classmethod
    def inserirNoCarrinho(cls):
        idProduto = int(input("Digite o ID do produto desejado: "))
        qtd = int(input("Digite a quantidade do produto desejado: "))
        vEst = View.verificarEstoque(idProduto, qtd)
        if (vEst == "ok"):
            View.inserirNoCarrinho(idProduto, qtd)
            print("\n\033[1;32mProduto inserido no carrinho!\033[m")
        else:
            print(vEst)

    @classmethod
    def verCarrinho(cls):
        carrinho = View.verCarrinho(cls.idClienteSessao)
        if (carrinho == None):
            print("\nCarrinho vazio.")
        else:
            print(25*"-")
            print("\033[1;33mCARRINHO\033[m")
            for item in carrinho:
                print(f'\033[1;33m{item}\033[m')

    @classmethod
    def atualizarCarrinho(cls):
        if not (View.verificarCarrinho(cls.idClienteSessao)):
            print("\nCarrinho vazio.")
        else:
            idProduto = int(input("Digite o ID do produto que deseja atualizar no carrinho: "))
            qtd = int(input("Digite a nova quantidade desejada do produto: "))
            if (View.verificarEstoque(idProduto, qtd) == "ok"):
                View.atualizarCarrinho(idProduto, qtd)
                print("\n\033[1;32mProduto atualizado no carrinho!\033[m")
            else:
                print(View.verificarEstoque(idProduto, qtd))

    @classmethod
    def removerDoCarrinho(cls):
        if not (View.verificarCarrinho(cls.idClienteSessao)):
            print("\nCarrinho vazio.")
        else:
            idProduto = int(input("Digite o ID do produto que deseja remover do carrinho: "))
            rdc = View.removerDoCarrinho(idProduto)
            if (rdc == False):
                print("\n\033[1;31mO produto do ID digitado não consta no carrinho.\033[m")
            else:
                print("\n\033[1;32mProduto removido do carrinho!\033[m")
        
    @classmethod
    def finalizarCompra(cls):
        if not (View.verificarCarrinho(cls.idClienteSessao)):
            print("\nCarrinho vazio.")
        else:
           op = int(input("Digite 1 para confirmar a finalização do pedido ou qualquer número para continuar comprando: "))
           if (op == 1):
            print(View.finalizarCompra(cls.idClienteSessao))


UI.main()
        
