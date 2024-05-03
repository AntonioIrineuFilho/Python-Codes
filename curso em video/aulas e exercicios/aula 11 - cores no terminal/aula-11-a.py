# '\033[style;text;backgroundm'
# style -> 0(normal), 1(negrito), 4(sublinhado), 7(invertido)
# text -> 30 a 37(branco, vermelho, verde, amarelo, azul, roxo, ciano e cinza)
# back -> 40 a 47(branco, vermelho, verde, amarelo, azul, roxo, ciano e cinza)
# \033[m -> Valor padrão do terminal, importante de colocar caso queria resetar a cor em alguma parte do codigo
x = input('\033[1;33mOlá, qual o seu nome? ')
if (x == 'Antônio'):
    print('\033[1;33mQue legal! Seu nome é \033[1;35m{}\033[m'.format(x))
else:
    print('\033[1;33mQue legal! Seu nome é \033[1;33m{}\033[m'.format(x))