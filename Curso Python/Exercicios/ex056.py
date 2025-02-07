#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa mostre: 
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas  mulheres tem menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehome = 0
nomevelho = " "
totmulher20 = 0
for i in range(1, 5):
    print(f"----- {i}º Pessoa -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if i == 1 and sexo in "Mm":
        maioridadehome= idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
            totmulher20 += 1
mediaidade = somaidade / 4
print(f"\nA média de idade do grupo é de {mediaidade} anos.")
print(f"O homem mais velho tem {maioridadehome} e se chama: {nomevelho}")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos.\n")
