"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a. Quantos números foram digitados. 
b. A lista de valores, ordenada de forma decrescente. 
c. Se o valor 5 foi digitado e está ou não na lista. """
lista = list()

while True:
    lista.append(int(input("Digite um valor: ")))

    opcao = str(input("Deseja continuar? [S/N]: "))
    if opcao in "Nn":
        print("Programa sendo encerrado...")
        break

print("=-=" * 15)

print(f"Foram digitados um total de {len(lista)} números.")

lista.sort(reverse=True)
print("Valores digitados (Invertidos): ", end="")

for l in lista:
    print(f"{l}... ", end="")
print()

if 5 in lista:
    print(f"O valor 5 foi digitado na lista.")
else:
    print("O valor 5 não foi digitado e cadastrado na lista.")
