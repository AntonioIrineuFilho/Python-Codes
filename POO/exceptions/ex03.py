try:
    with open("teste.txt", mode="r") as arquivo:
        input = arquivo.readlines()
except FileNotFoundError as erro:
    print(erro)

print("CONTINUA...")