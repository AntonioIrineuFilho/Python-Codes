n1 = float(input())
n2 = float(input())
media = (n1 + n2) / 2
if (media >= 6):
    print("APROVADO COM MÉDIA","{:.1f}".format(media))
elif (media < 6 and media >= 4):
    print("EM RECUPERAÇÃO COM MÉDIA","{:.1f}".format(media))
else:
    print("REPROVADO COM MÉDIA","{:.1f}".format(media))