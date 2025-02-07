#Um Professor que sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem a ser sorteada. 

import random

print("\nSeja bem-vindo, vamos organizar a lista de apresentação.\n")

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print("\n\nA ordem de apresentação será: \n")
print(alunos)