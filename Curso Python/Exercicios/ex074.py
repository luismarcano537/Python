"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados.
também indique o menor e o maior valor que estão na tupla."""
from random import randint

numeros = ((randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5)))
print("=-=" * 10)
print(f"Os números sorteados foram: ", end=" ")
for n in numeros: #Caso eu não queira mostrar no formato de tupla com parenteses e virgulas, posso utilizar um for, caso não tenha problema pode utilizar um print normal.
    print(f"{n} ", end= " ")
print(f"\nO maior número sorteado foi: {max(numeros)}")
print(f"O menor número sorteado foi: {min(numeros)}")
print("=-=" * 10)
