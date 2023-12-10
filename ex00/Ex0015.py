import math

op = float(input("Digite o valor do cateto oposto:"))
ad = float(input("Digite o valor do cateto adjacente"))

hp = math.hypot(op, ad)

print("No tirangulo retangulo no qual o cateto oposto vale {} e o adjacente {} a hipotenusa é {:.2f}".format(op, ad, hp))
