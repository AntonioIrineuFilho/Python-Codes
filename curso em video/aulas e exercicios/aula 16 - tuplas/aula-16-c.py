# tupla.count(numero/string) -> metodo para contar o total de aparições do valor na tupla
# tupla.index(numero/string) -> mostra o indice da primeira aparição do valor na tupla
# tupla.index(numero/string, posição) ->  mostra o indice da primeira aparição após a posição informada
# tuplas podem receber dados de tipos diferentes

lanche = ('hamburguer', 'batata', 'pizza', 'pudim', 'pudim', 'batata')

x = input('Digite um lanche: ').strip().lower()

if (lanche.count(x) == 0):
    print('Esse lanche está indisponível')
else:
    print(f'Existem {lanche.count(x)} unidades de {x} no estoque')

