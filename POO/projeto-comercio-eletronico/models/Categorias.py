import json

class Categoria:
    def __init__(self, id, descricao):
        self.setId(id)
        self.setDescricao(descricao)
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
        print(categoria)

    @classmethod
    def listarCategorias(cls):
        cls.abrir()
        return cls.categorias
    
    @classmethod
    def atualizarCategoria(cls, categoria):
        cls.abrir()
        for i in range(len(cls.categorias)):
            if (cls.categorias[i].getId() == categoria.getId()):
                cls.categorias[i].setDescricao(categoria.getDescricao())
                break
            if (i == len(cls.categorias)-1):
                print("Categoria não encontrada.")
                return
        cls.salvar()

    @classmethod
    def deletarCategoria(cls, id):
        cls.abrir()
        for i in range(len(cls.categorias)):
            if (cls.categorias[i].getId() == id):
                del(cls.categorias[i])
                break
            if (i == len(cls.categorias)-1):
                print("Categoria não encontrada.")
                return
        cls.salvar()

    @classmethod
    def abrir(cls):
        cls.categorias = []
        try:
            with open("json/categorias.json", mode="r") as arquivo:
                objetos = json.load(arquivo)
            for obj in objetos:
                c = Categoria(obj["_Categoria__id"], obj["_Categoria__descricao"])
                cls.categorias.append(c)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    @classmethod
    def salvar(cls):
        with open("json/categorias.json", mode="w") as arquivo:
            json.dump(cls.categorias, arquivo, default=vars)