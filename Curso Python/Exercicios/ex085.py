numeros = [[], []]

for n in range(0, 7):
    num = (int(input(f"Insira o {n+1}º número: ")))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print(f"Foram digitados os seguintes números pares: {numeros[0]}")
print(f"Foram digitados os seguintes números ímpares: {numeros[1]}")
print()
