"""Aprimore o desafio anterior, mostrando no final: 
a) A Soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
coltres = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f"Digite um valor para a posição {[l],[c]}: ")))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
 
print("=-=" * 10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()

for l in range(0, 3):
    coltres += matriz[l][2] 

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
      
print(f"A soma de todos os valores pares é: {soma}")
print(f"A soma dos valores da terceira coluna é: {coltres}")
print(f"O maior valor da segunda linha é: {maior}")
