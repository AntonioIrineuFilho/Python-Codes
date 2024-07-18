l2 = []

def primo_ini(n, d):
        if (n == 1 or d == 1):
             return 'Primo'
        elif (n % d == 0):
            return 'Não Primo'
        else:
            return primo_ini(n, d - 1)

def primo(n):
     return primo_ini(n, n-1)

def lista_primos_ini(l1, tamanho, inicial):
     global l2
     if (inicial == tamanho):
          return l2
     else:
          if (primo(l1[inicial]) == 'Primo'):
               l2.append(l1[inicial])
               return lista_primos_ini(l1, tamanho, inicial+1)
          else:
               return lista_primos_ini(l1, tamanho, inicial+1)
          
def lista_primos(l1):
     return lista_primos_ini(l1, len(l1), 0)

l1 = list(map(int, input().split()))
print(lista_primos(l1))