"""Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas."""
numeros = list()
pares = list()
impares = list()

while True:
    n = int(input("Digite um valor: "))
    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    opcao = str(input("Deseja continuar? [S/N]: ")).upper()
    if opcao in "Nn":
        print("Programa sendo encerrado...")
        break
    
print("=-=" * 15)
print(f"Listas geradas a partir dos dados inseridos: ")

print("Números cadastrados: ", end="")
for n in numeros:
    print(f"{n}... ", end="")
print()

print("Números pares cadastrados: ", end="")
for p in pares: 
    print(f"{p}... ", end="")
print()

print("Números ímpares cadastrados: ", end="")
for i in impares:
    print(f"{i}... ", end="")
print()
