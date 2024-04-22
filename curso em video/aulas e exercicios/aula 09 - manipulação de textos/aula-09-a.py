# fatiamento de string -> ao guardar uma string numa variavel, cada caracter fica salvo em um espaço de memoria, podendo ser encontrado por meio de um indice
# variavel[indice] -> localiza o caracter na posição
# variavel[x:y] -> localiza dos caracteres da posição x até y - 1
# variavel[x:y:z] -> localiza dos caracteres da posição x até y - 1, pulando de z em z
# variavel[:x] -> vai do caracter 0 até o caracter na posição x
# variavel[x:] -> vai do caracter na posição x até o caracter da ultima posição
# variavel[x::y] -> x até o ultimo, pulando de y em y
string = input('Digite uma frase: ')
print(string[3:7])
print(string[3:10:3])
print(string[3::7])