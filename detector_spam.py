email = input('Digite o email do rementente: ')

def detector_spam(email):
    for i in range(len(email)):
        if (email[i] == '@'):
            if (email[i:] == '@xyz.com'):
                return True
    return False

print(detector_spam(email))

