def primo(n: int, n_div: int) -> int:
        if (n % n_div == 0 and n_div != n and n_div != 1):
            return 'Não Primo'
        elif (n % n_div == 0 and n_div != n):
            return 'Primo'
        else:
            return primo(n, n_div - 1)

n = int(input('Digite um número natural: '))
print(f'O número {n} é: {primo(n, n)}')
