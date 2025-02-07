#Crie um programa que leia o nome de uma pessoa e informe se ele possui "SILVA".

nome = str(input("Digite seu nome: ")).strip()
nome.upper()

print(f"Seu nome, possui 'Silva'?: {'SILVA' in nome.upper()}")
      
