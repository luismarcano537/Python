#Escreva um programa que leia dois números inteiros e compare-os. 
#Mostre uma mensagem na tela informando: 1. O primeiro valor é maior. 2. O segundo valor é maior. Não existe valor maior, os dois são iguais.

print("=-=-=" *10)
print("Seja bem-vindo, vamos realizar a compração de números!")
print("=-=-=" *10)

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"\nO {num1} é maior que {num2}")
elif num2 > num1:
    print(f"\nO {num2} é maior que o {num1}")
elif num1 == num2:
    print(f"\nNão existe valor maior, os números {num1} e {num2} são iguais.")

print(f"\nObrigado por ter utilizado o sistema de comparação!\n")
