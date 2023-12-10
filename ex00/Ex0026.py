a = float(input("Qual a velocidade atual do veículo? "))

if a > 80:
	print("Reduza a velocidade para menos de 80km/h, voce sera multado.")
	m = (a- 80) * 7
	print("A sua multa ficara em R$",m)

elif a < 40:
	print("Aumente sua velocidade para mais de 40kh/h, voce sera multado")
	m2 = (40 - a) * 3
	print("A multa ficara em R$", m2)	
else:
	print("Tenha um otimo dia.")