#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input("Digite um número: "))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print("\033[33m", end= " ")
        tot += 1
    else:
        print("\033[31m", end= " ")
    print(f"{i}", end= " ")
print(f"\n\033[mO Número {num} foi divisível {tot} vezes.")
if tot == 2:
    print("\nE por isso ele É primo!\n")
else:
    print("\nE por isso ele NÃO é primo!\n")
