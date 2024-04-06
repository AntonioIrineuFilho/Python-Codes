# Para importar uma biblioteca inteira -> import biblioteca
# Para importar funcionalidades especificas -> from biblioteca import função
# Biblioteca math -> funções matemáticas, como:
# ceil(arredondamento pra cima), floor(arredondamento pra baixo)
# trunc(truncar o numero), pow(potencial), sqrt(raiz quadrada), fatorial
import math
n = int(input('Digite um número: '))
# Para usar uma função math -> math.função(valor/variavel)
print(math.sqrt(n))
print('{:.2f}'.format(math.pi*math.sqrt(n)))