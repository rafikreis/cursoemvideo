import random

p1 = str(input("Nome do 1° aluno:"))
p2 = str(input("Nome do 2° aluno:"))
p3 = str(input("Nome do 3° aluno:"))
p4 = str(input("Nome do 4° aluno:"))


alunos = [p1, p2, p3, p4]
random.shuffle(alunos)

print("A ordem de apresentação é:{}".format(print(alunos)))
