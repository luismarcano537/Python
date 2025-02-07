#Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números foram digitados 
# e qual foi a soma entre eles. 
import time as tm
print("~" * 30)
print("Leitor de números")
print("~" * 30)
contador = 0
soma = 0
print("""    Digite os números que deseja, 
      no final mostraremos a somatoria e quantos você inseriu!
      Digite 999 para encerrar o programa\n""")
n = int(input("Digite um número: "))
while n != 999:
    contador += 1
    soma += n 
    n = int(input(f"Digite um número: "))
print("Realizando calculos...")
tm.sleep(1)
print(f"Foram digitados {contador - 1} números e a soma entre eles foi: {soma}")
