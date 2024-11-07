from clientes import Clientes
import json

class UI:
    def cadastrarClientes():
        n = int(input("Digite quantos clientes deseja cadastrar: "))
        clientes = []
        for i in range(0, n):
            nome = input(f"Digite o nome do cliente {i+1}: ")
            sexo = input(f"Digite o gênero do cliente {i+1}: ")
            telefone = int(input(f"Digite o número de telefone do cliente {i+1}: "))
            cliente = Clientes(nome, sexo, telefone)
            clientes.append(cliente)

            with open("data.json", mode = "w") as arquivo:
                json.dump(clientes, arquivo, default = vars)
    def visualizarClientes():
        with open("data.json", mode = "r") as arquivo:
            clientes = json.load(arquivo)
        add_clientes_from_json = []
        for c in clientes:
            # print(c)
            # criar novos objetos com base nos valores do arquivo
            cliente = Clientes(c["nome"], c["sexo"], c["telefone"])
            add_clientes_from_json.append(cliente)
        for c in add_clientes_from_json:
            print(c) # -> printa, para cada objeto da lista, aquele metodo str criado na classe CLientes
    def main():
        print("1-Cadastrar clientes\n2-Visualizar clientes")
        op = int(input("Digite a opção desejada: "))
        if (op == 1):
            UI.cadastrarClientes()
        elif (op == 2):
            UI.visualizarClientes()
        else:
            print("Opção inválida.")
        
    
UI.main()


