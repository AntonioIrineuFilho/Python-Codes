# para receber dados de entrada de outro arquivo -> arquivo.py < entrada.extensao
# para usar no PowerShell o comando é: Get-Content entrada.extensao | python arquivo.py
# ex: python3 soma.py < e1.txt
n1 = int(input())
n2 = int(input())
soma = n1 + n2
print(soma)