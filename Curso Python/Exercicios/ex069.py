'''Crie eum programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantas homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.'''

opção = " "
Maior18 = 0
homens = 0
mulhermenor20 = 0

while True:
    idade = int(input("Digite a idade do usuári@: "))
    sexo = str(input("Digite o sexo: [M/F] ")).strip().upper()[0]
    while sexo not in "MF":
        sexo = str(input("Digite o sexo: [M/F] ")).strip().upper()[0]

    if idade > 18:
        Maior18 += 1
    if sexo == "M":
        homens += 1
    if idade < 20 and sexo == "F":
        mulhermenor20 += 1
    
    opção = str(input("Deseja continuar?: [S/N]")).strip().upper()[0]
    while opção not in "SN":
        opção = str(input("Deseja continuar?: [S/N] ")).strip().upper()[0]
    
    if opção == "S":
        print("Perfeito... Vamos continuar.")
    else:
        print("Programa sendo encerrado...")
        break

print(f"Foram cadastradas {Maior18} pessoas maior de idade.", end= " ")
print(f"Foram cadastrados {homens} homens.", end= " ")
print(f"Foram cadastradas {mulhermenor20} mulheres menores de 20 anos.")
print("\nAté mais...")
