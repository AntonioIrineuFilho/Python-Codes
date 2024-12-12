from view import View

class UI:
    @staticmethod
    def menu():
        print(15*"-")
        print("MENU DO ADMIN")
        print(15*"-")
        print("1-Inserir Cliente\n2-Listar Clientes\n3-Atualizar Cliente\n4-Deletar Cliente\n")
        print("5-Inserir Categoria\n6-Listar Categorias\n7-Atualizar Categoria\n8-Deletar Categoria\n")
        print("9-Inserir Produto\n10-Listar Produtos\n11-Atualizar Produtos\n12-Deletar Produtos\n")
        print("13-Sair\n")
        op = int(input("Digite a opção desejada: "))
        return op
    
    @staticmethod
    def main():
        run = True
        while (run):
            match(UI.menu()):
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
        desc = input("Digite a descrição do produto")
        preco = float("Digite o preço do produto: ")
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
            desc = input("Digite a descrição do produto")
            preco = float("Digite o preço do produto: ")
            estoque = int(input("Digite a quantidade em estoque: "))
            idCategoria = int(input("Digite o ID da categoria do produto: "))
            View.atualizarProduto(id, desc, preco, estoque, idCategoria)
    
    @classmethod
    def deletarProduto(cls):
        produtos = View.listarProdutos()
        if (len(produtos) == 0):
            print("Nenhum produto cadastrado.")
        id = int(input("Digite o ID do produto que deseja atualizar: "))
        if not (View.validarProdutoId(id)):
            print("Produto não encontrado.")
        else: 
            View.deletarProduto(id)     

        
        


UI.main()
        
