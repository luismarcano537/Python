#Faça um programa que mostre na tela um contagem regressiva para o 
# estouro de fogos de atificio.
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print("=-=-=" * 10)
print("Contagem regressiva para os fogos aritificais.")
print("=-=-=" * 10)

for i in range(10, -1, -1):
    print(i)
    sleep(1)

print("\nBoom! Estouraram os fogos artificiais.\n")
#Fim. 