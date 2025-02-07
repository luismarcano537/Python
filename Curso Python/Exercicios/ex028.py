#Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5. 
#O usuário deve tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu. 
import random
print("=-=" * 10)
print("Jogo de adivinhança")
print("=-=" * 10)

print("\nEu vou pensar em um número e você irá tentar adivinhar qual número eu pensei do 0 ao 5")

n_aleatorio = random.randint

n_jogador = int(input("Digite um número do 0 ao 5: "))

if n_aleatorio == n_jogador:
    print("Parabéns! Você acertou.")
else:
    print("Errou, tente novamente!\n")
