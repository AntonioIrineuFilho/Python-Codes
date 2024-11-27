class Musica:
    def __init__(self, titulo, artista, album):
        self.setTitulo(titulo)
        self.setArtista(artista)
        self.setAlbum(album)
    def setTitulo(self, titulo):
        if (titulo == ""):
            raise ValueError("INVALID TITLE")
        else:
            self.__titulo = titulo
    def setArtista(self, artista):
        if (artista == ""):
            raise ValueError("INVALID ARTIST")
        else:
            self.__artista = artista
    def setAlbum(self, album):
        if (album == ""):
            raise ValueError("INVALID ALBUM")
        else:
            self.__album = album
    def getTitulo(self):
        return self.__titulo
    def getArtista(self):
        return self.__artista
    def getAlbum(self):
        return self.__album
    def __str__(self):
        return f'\nTítulo: {self.__titulo}\nArtista: {self.__artista}\nÁlbum: {self.__album}\n'