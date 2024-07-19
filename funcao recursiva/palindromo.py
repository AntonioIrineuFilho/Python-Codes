def palindromo_ini(string, tamanho, inicial):
    if (inicial == tamanho//2):
        return 0
    else:
        if (string[inicial] == string[len(string)-inicial-1]):
            return 1 + palindromo_ini(string, tamanho, inicial+1)
        else:
            return 0 + palindromo_ini(string, tamanho, inicial+1)

def palindromo(string):
    if (palindromo_ini(string, len(string), 0) == len(string)//2):
        return True
    else:
        return False
    
string = input().strip().lower().split()
string = ''.join(string)

print(palindromo(string))
        