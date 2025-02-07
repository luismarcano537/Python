#Faça um programa que leia o sexo de uma pessoa, mas só aceite “M” ou “F”. Caso esteja errado, 
# peça a digitação novamente até ter um valor correto. 
sexo = str(input("Digite seu sexo: [M/F] ")).strip().upper()[0]

while sexo not in "FfMm":
    sexo = str(input("Dados inválidos. Digite seu sexo novamente: [M/F] ")).strip().upper()[0]
print(f"Sexo {sexo} cadastrado com sucesso.")
