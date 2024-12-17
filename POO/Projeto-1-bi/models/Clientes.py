import json

class Cliente:
        def __init__(self, id, nome, fone, email, senha):
                self.setId(id)
                self.setNome(nome)
                self.setFone(fone)
                self.setEmail(email)
                self.setSenha(senha)
        def setId(self, id):
            if (id < 0):
                raise ValueError("INVALID ID")
            else:
                self.__id = id
        def setNome(self, nome):
            if (nome == ""):
                raise ValueError("INVALID NAME")
            else:
                 self.__nome = nome
        def setFone(self, fone):
            if (fone == ""):
                raise ValueError("INVALID PHONE")
            else:
                 self.__fone = fone
        def setEmail(self, email):
             if (email == ""):
                raise ValueError("INVALID EMAIL")
             else:
                  self.__email = email
        def setSenha(self, senha):
            if (senha == ""):
                raise ValueError("INVALID PASSWORD")
            else:
                 self.__senha = senha
        def getId(self):
            return self.__id
        def getNome(self):
            return self.__nome
        def getFone(self):
            return self.__fone
        def getEmail(self):
            return self.__email
        def getSenha(self):
            return self.__senha
        def __str__(self):
            return f'{self.getId()} - {self.getNome()} - {self.getFone()} - {self.getEmail()}'

class Clientes:
    clientes = []

    @classmethod
    def inserirCliente(cls, cliente):
        cls.abrir()
        if not (cliente.getEmail() == "admin" and cliente.getSenha() == "admin"):
            id = 0
            for obj in cls.clientes:
                if (obj.getId() >= id):
                    id = obj.getId()
            cliente.setId(id+1)
        cls.clientes.append(cliente)
        cls.salvar()
    
    @classmethod
    def listarClientes(cls):
        cls.abrir()
        return cls.clientes

    @classmethod
    def atualizarCliente(cls, cliente):
        cls.abrir()
        for i in range(len(cls.clientes)):
            if (cls.clientes[i].getId() == cliente.getId()):
                cls.clientes[i].setNome(cliente.getNome())
                cls.clientes[i].setFone(cliente.getFone())
                cls.clientes[i].setEmail(cliente.getEmail())
                cls.clientes[i].setSenha(cliente.getSenha())
                break
            if (i == len(cls.clientes) - 1):
                print("Cliente não encontrado.")
                return
        cls.salvar()
    
    @classmethod
    def deletarCliente(cls, id):
        cls.abrir()
        for i in range(len(cls.clientes)):
            if (cls.clientes[i].getId() == id):
                del(cls.clientes[i])
                break
            if (i == len(cls.clientes)-1):
                print("Cliente não encontrado.")
                return
        cls.salvar()

    @classmethod
    def salvar(cls):
        with open("json/clientes.json", mode="w") as arquivo:
            json.dump(cls.clientes, arquivo, default=vars)
    
    @classmethod
    def abrir(cls):
        cls.clientes = []
        try:
            with open("json/clientes.json", mode="r") as arquivo:
                objetos = json.load(arquivo)
            for obj in objetos:
                c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__fone"], obj["_Cliente__email"], obj["_Cliente__senha"])
                cls.clientes.append(c)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass