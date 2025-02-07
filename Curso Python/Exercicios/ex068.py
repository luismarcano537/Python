'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
vitorias = 0 

while True:
    jogador = int(input("Digite um número: "))
    computador = randint(0, 11)
    total = jogador + computador
    
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar?: [P/I]")).strip().upper()
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}", end=" ")
    print(" Deu PAR!" if total % 2 == 0 else "Deu ÍMPAR!")

    if tipo == "P":
        if total % 2 == 0:
            print("Você venceu!")
            vitorias += 1
        else:
            print("Você perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você venceu!")
            vitorias += 1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER!!! Você venceu {vitorias} vezes.")