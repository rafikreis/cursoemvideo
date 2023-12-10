import random

a1 = str(input("O primeiro aluno é:"))
a2 = str(input("O segundo aluno é:"))
a3 = str(input("O terciro aluno é:"))
a4 = str(input("O quarto aluno é:"))

lista = [a1, a2, a3, a4]

esc = random.choice(lista)

print("Dentre os 4 alunos, o(a) escolhido(a) foi", esc)
