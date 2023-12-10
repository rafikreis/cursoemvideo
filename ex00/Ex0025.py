from random import uniform

print("Vou pensar em um número entre 0 e 10, tente adivinhar")

a = int(input("Qual número voce pensou?"))
b = int(uniform(0, 10))

if b == a:
	print("Voce ganhou")
else:
	print("Voce perdeu, o número que pensei foi {}".format(b))
