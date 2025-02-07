#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
#Se ele ainda vai se alistar ao serviço militar, se é a hora de alistar ou se já passou do tempo de alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import time
import datetime

print("\nSeja bem-vindo, vamos verificar sua situação militar.\n")
nome = input("Digite seu nome: ")
ano_atual = int(input("Digite o ano atual: "))
nascimento = int(input("Digite seu ano de nascimento: "))
idade = (ano_atual - nascimento)

print("\nAnalisando informações...")
time.sleep(1)

if idade < 18:
    print("\nVocê é menor de idade.")
    print(f"Faltam {abs(18 - idade)} anos para você se alistar em {nascimento + 18}.\n")
elif idade == 18:
    print("Você deve se alistar IMEDIATAMENTE.\n")
elif 18 <= idade <= 45:
    print(f"\n{nome}, Você deve se alistar.")
    print(f"Você possuí {abs(idade - 18)} anos atrassado.")
    print(f"Você devia se alistar em {nascimento + 18}\n")
else:
    print("\nVocê é idoso, não precisa se alistar.\n")

print("Obrigado por ter utilizado nosso sistema.")