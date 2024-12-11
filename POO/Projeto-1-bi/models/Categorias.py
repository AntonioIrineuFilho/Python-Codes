import json

class Categoria:
    def __init__(self, id, descricao):
        self.setId(id)
        self.setDescricao
    def setId(self, id):
        if (id < 0):
            raise ValueError("INVALID ID")
        else:
            self.__id = id
    def setDescricao(self, descricao):
        if (descricao == ""):
            raise ValueError("INVALID DESCRIPTION")
        else:
            self.__descricao = descricao
    def getId(self):
        return self.__id
    def getDescricao(self):
        return self.__descricao
    def __str__(self):
        return f'{self.getId()} - {self.getDescricao()}'


class Categorias:
    categorias = []

    @classmethod
    def inserirCategoria(cls, categoria):
        cls.abrir()
        id = 0
        for obj in cls.categorias:
            if (obj.getId() > id):
                id = obj.getId()
        categoria.setId(id+1)
        cls.categorias.append(categoria)
        cls.salvar()

    @classmethod
    def listarCategorias(cls):
        cls.abrir()
        return cls.categorias
    
    @classmethod
    def atualizarCategoria(cls, categoria):
        cls.abrir()
        for i in range(len(cls.categorias)):
            if (cls.categorias[i].getId() == categoria.getId()):
                cls.categorias[i].setDescricao(categoria.getDescricao)
            if (i == len(cls.categoria)-1):
                return "Categoria não encontrada."
        cls.salvar()

    @classmethod
    def deletarCategoria(cls, id):
        cls.abrir()
        for i in range(len(cls.categorias)):
            if (cls.categoria[i].getId() == id):
                cls.categorias.remove(cls.categoria[i])
        cls.salvar()

    @classmethod
    def abrir(cls):
        cls.categorias = []
        with open("categorias.json", mode="r") as arquivo:
            objetos = json.load(arquivo)
        for obj in objetos:
            c = Categoria(obj["id"], obj["descricao"])
            cls.categorias.append(c)

    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.categorias, arquivo, default=vars)