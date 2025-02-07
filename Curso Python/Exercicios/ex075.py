"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final mostre, quantas vezes apareceu o valor 9.
Em que posição foi digitado o primeiro valor 3.
Quais foram os números pares."""

numeros = (int(input("\nDigite o primeiro valor: ")), int(input("Digite o segundo número: ")), 
           int(input("Digite o terceiro valor: ")), int(input("Digite o quarto número: ")))

"""numeros = tuple(int(input("Digite um número: ")) for _ in range(4)) #Caso eu queira automaizar a inserção."""

print(f"\nOs números digitados foram: ", end= " ")
for n in numeros:
    print(f"{n}", end= " ")

print(f"\nO número 9 apareceu {numeros.count(9)} vezes.")

if 3 in numeros:
    print(f"O número 3 foi digitado na {numeros.index(3)+1}ª posição.")
else:
    print("O número 3 não foi digitado.")

pares = tuple(n for n in numeros if n % 2 == 0)
print("Os números pares inseridos foram:", end=" ")
for p in pares:
    print(f"{p}", end=" ")
