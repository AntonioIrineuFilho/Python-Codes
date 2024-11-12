class Cliente:
    def __init__(self, nome, conta, saldo):
        self.nome = str(nome)
        self.conta = int(conta)
        self.saldo = float(saldo)
    def Deposito(self, acrescimo):
        self.saldo += acrescimo
    def Saque(self, retirado):
        self.saldo -= retirado
    def getSaldo(self):
        return self.saldo

cliente1 = Cliente("João", 12345, 600)
cliente2 = Cliente("Amanda", 12346, 1400)
cliente3 = Cliente("Carlos", 12347, 10000)
clientes = [cliente1, cliente2, cliente3]
n = input("Digite seu nome: ")
nc = int(input("Digite o número da conta: "))
verificador = False
for c in clientes:
    if (c.nome == n and c.conta == nc):
        verificador = True
        cliente_now = c
        break
if not (verificador):
    print("Cliente não identificado.")
    quit()
else:
    print("Cliente identificado com sucesso.")
    print("1-Depositar\n2-Sacar\n3-Ver Saldo")
    op = int(input(("Digite a opção desejada: ")))
    if (op == 1):
        valor = float(input(("Digite o valor do depósito: ")))
        cliente_now.Deposito(valor)
        print(f'Depósito efetuado com sucesso.\nSaldo atual: R$ {cliente_now.getSaldo():.2f}')
    elif (op == 2):
        valor = float(input(("Digite o valor do saque: ")))
        cliente_now.Saque(valor)
        print(f'Saque efetuado com sucesso.\nSaldo atual: R$ {cliente_now.getSaldo():.2f}')
    elif (op == 3):
        print(f'Saldo atual: R$ {cliente_now.getSaldo():.2f}')
    else:
        print("Opção inválida.")