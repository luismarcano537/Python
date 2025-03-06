"""Crie um programa que crie uma matriz de dimensão 3X3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta."""

Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        Matriz[l][c] = (int(input(f"Digite um valor para a posição {[l], [c]}: ")))

print("=-=" * 10)
print("Matriz 3X3 gerada: \n")
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{Matriz[l][c]:^5}]", end="")
    print()

