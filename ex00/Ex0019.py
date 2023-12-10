nome = str(input("Digite seu nome completo:")).strip()

Mai = nome.upper()
Min = nome.lower()

num = nome.__len__()
space = nome.count(' ')
separa = nome.split()

print("Seu nome em maiusculas {},\n e em minusculas é {},\n e tem {} letras.".format(Mai, Min, num - space, ))
print("Seu 1° nome é {} e tem {} letras".format(separa[0], len(separa[0])))
