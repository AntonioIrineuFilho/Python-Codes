from Musica import Musica

class Playlist:
    def __init__(self, nome, desc):
        self.__musicas = []
        self.setNome(nome)
        self.setDescricao(desc)
    def setNome(self, nome):
        if (nome == ""):
            raise ValueError("INVALID NAME")
        else:
            self.__nome = nome
    def setDescricao(self, desc):
        if (desc == ""):
            raise ValueError("INVALID DESCRIPTION")
        else:
            self.__desc = desc
    def getNome(self):
        return self.__nome
    def getDescricao(self):
        return self.__desc
    def Inserir(self, musica):
        self.__musicas.append(musica)
    def Listar(self):
        return self.__musicas
    def __str__(self):
        return f'Número de músicas: {len(self.__musicas)}'