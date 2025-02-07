#Faça um programa que leia o nome de uma pessoa e mostre o primeiro nome e o ultimo nome enseguidamente.

nome = str(input("Digite seu nome completo: ")).strip().upper()

print("\nAnalisando seu nome...")
print(f"Seu nome completo é {nome}")
n = nome.split()

print(f"\nSeu primeiro nome é {n[0]}")
print(f"Seu ultimo nome é {n[len(n) -1]}") #O -1 permite indicar que acessamos ao ultimo item da lista n.

print("\n\nObrigado por ter utilizado o nosso algoritmo!\n")

#Acabou, foda-se...