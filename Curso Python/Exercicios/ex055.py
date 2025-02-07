#Faça um programa que leia o peso de cinco pessoas e no final mostre qual 
#foi o maior e o menor dos peso lidos.
peso = []
for i in range(1, 6):
    peso.append(float(input(f"\nDigite o peso da {i}º pessoa: ")))

maior = max(peso)
menor = min(peso)

print(f"\nO maior peso informado foi: {maior:.2f}kg e o menos peso informado foi: {menor:.2f}kg")
 