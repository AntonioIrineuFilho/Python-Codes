div = []

def divisores_ini(n, d):
    global div
    if (d == 1):
        div.append(d)
        return div
    else:
        if (n % d == 0):
            div.append(d)
            return divisores_ini(n, d-1)
        else:
            return divisores_ini(n, d-1)
        
def divisores(n):
    return divisores_ini(n, n)

n = int(input())

print(divisores(n))