# dicionario = dict()
# dados = {'nome':'Pedro', 'idade':34}
# para declarar dicionarios usam-se chaves
# os atributos funcionam como indices, ao chamar um atributo, chamam-se os parametros dele
# pode-se criar novos atributos e atribuir valores a eles
# .value() -> mostra os parametros
# .keys() -> mostra os atributos
# .items() -> mostra tudo
dados = {'nome':'Pedro', 'idade':34}
dados['sexo'] = 'M'
print(dados['nome'])
print(dados['sexo'])
print(dados.values())
print(dados.keys())
print(dados.items())