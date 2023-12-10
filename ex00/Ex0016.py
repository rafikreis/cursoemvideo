import math

a = float(input("Digite um angulo:"))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))

print("Para o angulo {} seu seno é {} seu coseno {} e sua tangente {}".format(a, sen, cos, tg))
