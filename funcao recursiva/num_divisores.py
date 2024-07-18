def div(n: int, n_div: int) -> int:
    if (n_div == 1):
        return 1
    else:
        if (n % n_div == 0):
            return 1 + div(n, n_div - 1)
        else:
            return 0 + div(n, n_div - 1)
        
n = int(input('Digite um número natural: '))
print(f'O número {n} possui {div(n, n)} divisores')
        