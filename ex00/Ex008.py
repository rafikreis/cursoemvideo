n = float(input("Qual a sua altura em metros?"))

dm = n * 10
cm = n * 100
mm = n * 1000
km = n / 1000
hm = n / 100
dam = n / 10

print("Sua altura em metros é igual a {}m".format(n))
print("Já sua alrua em cm é {}, e em mm é {}, e em dm é {}".format(cm, mm, dm))
print("Mas também sua alrua em km é {:.5f}, e em hm é {:.3f}, e em dam é {:.2f}".format(km, hm, dam))
