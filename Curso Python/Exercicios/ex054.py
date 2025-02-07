#Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
maior_idade = 0
menor_idade = 0
anos = []

for i in range(1, 8):
    nascimento = int(input(f"Digite o ano de nascimento da {i} ° pessoa: "))
    idade = atual - nascimento
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
    anos.append(nascimento)

print(f"Anos inseridos: {anos}")
print(f"{maior_idade} pessoas são maior de idade!")    
print(f"{menor_idade} pessoas são menor de idade!\n")
