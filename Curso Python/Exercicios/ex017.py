#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa. 
import math
print("Olá, me diga o comprimento do cateto oposto e adjacente e lhe informarei a hipotenusa!")

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa é: {hipotenusa:.2f}")

#Acabou. 