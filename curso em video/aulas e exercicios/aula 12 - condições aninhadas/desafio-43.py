h = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
imc = p / h ** 2
if (imc < 18.5):
    print('Você está abaixo do peso! Seu IMC deu {:.2f}'.format(imc))
elif (imc <= 25):
    print('Você está no peso ideal! Seu IMC deu {:.2f}'.format(imc))
elif (imc <= 30):
    print('Você está acima do peso! Seu IMC deu {:.2f}'.format(imc))
elif (imc <= 40):
    print('Você está com obesidade! Seu IMC deu {:.2f}'.format(imc))
else:
    print('Você está com obesidade mórbida! Seu IMC deu {:.2f}'.format(imc))