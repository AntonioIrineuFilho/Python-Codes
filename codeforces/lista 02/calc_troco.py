valor_item = int(input())
quant_itens = int(input())
valor_pago = int(input())
valor_total = valor_item * quant_itens
troco = valor_pago - valor_total
print("A pagar: ", valor_total, sep="")
print("Troco  : ", troco, sep="")
