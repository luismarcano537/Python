#Um professor quer sortear um dos seus quatros alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

print("Seja bem-vindo, vamos escolher um dos alunos, digite o nome de cada um por favor!")

aluno1 = str(input("\nDigite o nome do primeiro aluno: "))
aluno2 = str(input("Digite o nome do segundo aluno: "))
aluno3 = str(input("Digite o nome do terceiro aluno: "))
aluno4 = str(input("Digite o nome do quarto aluno: "))
aluno5 = str(input("Digite o nome do quinto aluno: "))

alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]

print("\n\nVamos escolher o aluno que irá apagar o quadro!")
print(f"O aluno escolhido é {random.choice(alunos)}\n")

#Acabou.
