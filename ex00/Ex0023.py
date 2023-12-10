x = str(input("Digite uma frase qualuquer:")).upper().strip()

print("A frase tem {} As".format(x.count('A')))
print("A primeira letra A aparece na posição {}".format(x.find('A')))
print("A última letra A aparece na posição {}".format(x.rfind('A')))
