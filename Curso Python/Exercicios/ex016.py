#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math

print("Olá, serei seu programa para transformar um número float para int.")
num = float(input("Me diga um número decimal: "))

print(f"O número digitado foi {num} e seu inteiro é: {math.trunc(num)}") #Podemos utilizar também a função int()

#Acabou.