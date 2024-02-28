n1 = float(input("Digite sua nota 1: "))
n2 = float(input("Digite sua nota 2: "))
media = (n1*2 + n2*3)/5
media_form = "{:.1f}".format(media)
print("Sua média é", media_form)