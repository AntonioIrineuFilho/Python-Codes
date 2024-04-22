# variavel.replace('x', 'y') -> substitui a informação de x por y
# variavel.upper() -> deixa tudo maiusculo
# variavel.lower() -> deixa tudo minusculo
# variavel.capitalize() -> deixa a primeira letra maiuscula
# variavel.title() -> deixa a primeira letra de cada palavra maiucula
# variavel.strip() -> remove os espaços inuteis antes e depois da string
# variavel.rstrip() -> remove os espaços do final
# variavel.lstrip() -> remove os espaços do inicio
x = input('Digite uma frase: ')
y = x.replace('bom dia', 'boa tarde')
print(y)