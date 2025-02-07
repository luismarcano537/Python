"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""
import time

valores = []
n = 0

while True:
    n = int(input("\nDigite um número: "))

    if n in valores:
        print(f"\nO valor {n} duplicado, não será adicionado.")
    else:
        valores.append(n)
        print(f"O valor {n} foi adicionado com sucesso.")

    opcao = str(input("\nDeseja continuar? [S/N]: ")).upper()
    if opcao == "N":
        print("Programa sendo encerrado.")
        break

valores.sort()

print("\nValores cadastrados: ")
for v in valores:
    print(f"{v}...", end="")
