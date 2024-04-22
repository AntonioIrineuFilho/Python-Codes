# len(variavel) -> conta a quant de caracteres da string
# variavel.count('') -> conta a quant de um caracter especifico 
# variavel.count('', x, y) -> faz a contagem do caracter indo da posição x até a posição y - 1
# variavel.find('') -> identifica a posição em que começa uma sequencia de caracteres
# '' in variavel -> mostra true ou false para a sequencia de caracteres
x = input('Digite uma frase: ')
print(len(x))
print(x.count('a'))
print(x.find('Ola'))