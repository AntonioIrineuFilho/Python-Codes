from Musica import Musica
from Playlist import Playlist
import json

class UI:
    def CriarPlaylist():
        nome = input("Digite o nome da playlist: ").strip().upper()
        desc = input("Digite uma descrição para a playlist: ").strip().upper()
        playlist = Playlist(nome, desc)
        print(f'Playlist {nome} criada com sucesso!')
        with open("playlist.json", mode = "w") as arquivo:
            json.dump(playlist, arquivo, default = vars)
    def InserirMusica():
        with open("playlist.json", mode = "r") as arquivo:
            pl = json.load(arquivo)
        if (len(pl) == 0):
            print("A playlist não foi criada.")
        else:
            playlist = Playlist(pl["_Playlist__nome"], pl["_Playlist__desc"])
            for i in range(len(pl["_Playlist__musicas"])):
                playlist.Inserir(pl["_Playlist__musicas"][i])
            n = int(input("Digite quantas músicas deseja inserir: "))
            for m in range(n):  
                titulo = input("Digite o título da música: ").strip().upper()
                artista = input("Digite o artista da música: ").strip().upper()
                album = input("Digite o álbum da música: ").strip().upper()
                musica = Musica(titulo, artista, album)
                playlist.Inserir(musica)
            with open("playlist.json", mode = "w") as arquivo:
                json.dump(playlist, arquivo, default = vars)
        
    def VerPlaylist():
        with open("playlist.json", mode = "r") as arquivo:
            pl = json.load(arquivo)
        if (len(pl) == 0):
            print("A playlist não foi criada.")
        else:
            playlist = Playlist(pl["_Playlist__nome"], pl["_Playlist__desc"])
            for i in range(len(pl["_Playlist__musicas"])):
                msc = pl["_Playlist__musicas"][i]
                musica = Musica(msc["_Musica__titulo"], msc["_Musica__artista"], msc["_Musica__album"])
                playlist.Inserir(musica)
            print("Músicas:\n", *playlist.Listar())
        
    def main():
        while True:
            print("1-Criar playlist\n2-Inserir música\n3-Ver playlist\n4-Sair")
            op = int(input("Digite a opção desejada: "))
            match (op):
                case 1:
                    UI.CriarPlaylist()
                case 2:
                    UI.InserirMusica()
                case 3:
                    UI.VerPlaylist()
                case 4:
                    print("FIM DE EXECUÇÃO.")
                    break
                case _:
                    print("OPÇÃO INVÁLIDA.")

UI.main()