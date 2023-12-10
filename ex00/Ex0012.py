p = float(input("Qual o preço original do produto em reais?"))
d = float(input("Qual o desconto percentual do produto?"))

dr = d/100

pd = p - (p * dr)

print("Antes o produto custava R${} é agora custa R${}".format(p, pd))
