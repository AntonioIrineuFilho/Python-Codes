# carro.siga() -> carro = objeto / .siga() = metodo
# todos os comandos são executados obrigatoriamente em ordem = estrutura sequencial
# comandos são executados com base em requisitos = estrutura condicional
# se carro.esquerda() -> comandos especificos serão executados
# se carro.direita() -> outros comandos serão executados
# if (carro.esquerda()):
#   bloco True
# else:
#   bloco False
# tem como realizar uma condicional em apenas uma linha ->
# print('carro novo' if tempo <= 3 else 'carro velho')
tempo = int(input('Quantos anos possui seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')