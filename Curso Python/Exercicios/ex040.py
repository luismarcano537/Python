#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida.: 
# 5.0 reprovado. 5.0 e 6.9 recuperação. 7.0 ou acima Aprovado.

print("\nInforme suas notas para saber sua média e sua situação atual.\n")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media <= 5.0:
    print(f"Sua média foi: {media}")
    print("\nVocê foi REPROVADO!")
elif 5.0 <= media <= 6.9:
    print(f"Sua média foi: {media}")
    print("\nVocê se encontra em RECUPERAÇÃO!")
else:
    print(f"\nSua média foi: {media}")
    print("Você foi aprovado")

print("\nObrigado por ter utilizado nosso sistema. \n")
