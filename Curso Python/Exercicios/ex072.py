"""Crie um programa que tenha uma tupla totalmente preenchida com uma 
contagem por extenso de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e vinte) e mostrá-lo por extenso."""
import time as tm

numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

print("=-=-=" * 10)
print("Números por extensos")
print("=-=-=" * 10)

while True:
    try:
        cont = int(input("Digite um número ou digite -1 para sair [0 a 20]: "))
        
        if cont == -1:
            print(f"Você selecionou {cont}, programa será encerrado.")
            tm.sleep(1)
            print("Programa encerrado.")
            break

        while cont < 0 or cont > 20:
            cont = int(input("Tente novamente, digite um número de 0 até 20: [0 até 20]"))

        if cont > 0 or cont < 20:
            print(f"O número {cont} por extenso é {numeros[cont]}.")

    except ValueError:
        print("Por favor, insira um número de 0 até 20!")
