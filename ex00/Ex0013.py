s = float(input("Qual seu atual salário em reais?"))
p = float(input("Qual promoçao que você acredita que merece?"))

per = p/100

pr = s + (s * per)

print("Antes seu salário era de R${} é agora é de R${}".format(s, pr))
