#Melhore o jogo do Desafio 28 onde o computador vai pensar em um número entre 0 a 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessário para vencer.
import random
import time
print("=-=-=" * 10)
print("Jogo da adivinhança, bem vindo!")
print("=-=-=" * 10)

print("\nO computador irá pensar em um número de 1 até 10 e você tentará acertar!")
print("Você terá varias tentativas para acertar.")

n_computador = random.randint(1, 10)
n_jogador = int(input("\nQual número o computador escolheu? "))
n_tentativas = 1
print("Analizando resposta... Espere...")
time.sleep(1)
while n_computador != n_jogador:
    if n_computador > n_jogador:
        print("\nHmm... não, o número é maior.")
    else:
        print("\nHmmm... não, o número é menor.")
    n_jogador = int(input("\nVocê errou, tente novamente: "))
    if n_computador != n_jogador:
        print("Analizando resposta... Espere...")
        time.sleep(1)
    n_tentativas += 1
print(f"\nParabéns! você acertou na {n_tentativas}º tentativa! O computador pensou em {n_computador}!\n")
