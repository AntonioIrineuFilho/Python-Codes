class Clientes:
    def __init__(self, nome, sexo, telefone):
        self.setNome(nome)
        self.setSexo(sexo)
        self.setTelefone(telefone)
    def setNome(self, nome):
        if (nome == ""):
            raise ValueError("VOID NAME NOT ALLOWED");
        else:
            self.nome = nome
    def getNome(self):
        return self.nome
    def setSexo(self, sexo):
        if (sexo == ""):
            raise ValueError("VOID GENDER NOT ALLOWED")
        else:
            self.sexo = sexo
    def getSexo(self):
        return self.sexo
    def setTelefone(self, telefone):
        if (telefone == 0):
            raise ValueError("NULL VALUE NOT ALLOWED")
        elif (telefone < 0):
            raise ValueError("NEGATIVE VALUE NOT ALLOWED")
        else:
            self.telefone = telefone
    def getTelefone(self):
        return self.telefone
    def __str__(self):
        return f'Nome = {self.nome}\nSexo = {self.sexo}\nTelefone = {self.telefone}'

  
        