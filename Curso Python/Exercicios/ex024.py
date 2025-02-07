#Crie um programa que leia o nome de uma cidade, diga se ela começa ou não com o nome "Santo". 
cidade = str(input("\nDigite o nome de uma cidade: ")).strip()

print(f"A cidade {cidade} começa com SANTO? {cidade[:5].upper() == "SANTO"}")
#Acabou.