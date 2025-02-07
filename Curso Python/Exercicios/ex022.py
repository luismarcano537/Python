#Faça um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (Sem considerar espaços).
#Quantas letras tem o primeiro nome. 

nome = str(input("\nDigite seu nome: ")).strip()
print("Analisando seu nome...")

print(f"\nSeu nome em maiúsculsa é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")

print(f"Seu nome tem um total de {len(nome) - nome.count(" ")} letras")

separado = nome.split()

print(f"Seu primeiro nome é {separado[0]} e tem {len(separado[0])} letras.")

#Acabou, fodase...