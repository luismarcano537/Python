#Faça um programa que leia três número e mostre qual é o maior e qual é o menor. 
import time
print("\nDigite 03 números e eu informarei qual é o menor e maior entre eles.")

a = int(input("\nDigite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))

print("\nAnalisando...")
time.sleep(3)

#Verificar o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b: 
    menor = c

#Verificar o maior
maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f"\nO número menor é {menor}.")
print(f"O número maior é {maior}.")
