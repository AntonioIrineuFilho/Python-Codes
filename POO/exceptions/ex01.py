try:
    x = int(input())
    print(x)
except:
    raise ValueError("NON INTEGER")

# try / except -> tenta executar um bloco de instruções. em caso de erro, redireciona para outro bloco de código dentro do except

# o except pode ser complementado com um código de erro especifico

# raise erro -> mostra o erro especificado, podendo conter uma string

# finally -> roda um código independentemente de erros