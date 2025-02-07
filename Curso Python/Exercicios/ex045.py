#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print(""""Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURSA""")

jogador = int(input("\nQual é a sua jogada? "))
print("=-=" * 10)
print(f"Computador jogou: {itens[computador]}")
print(f"O jogador jogou: {itens[jogador]}")
print("=-=" * 10)

if computador == 0:
    if jogador == 0:
        print("\nEMPATE.")

    elif jogador == 1:
        print("\nJOGADOR VENCEU.")

    elif jogador == 2:
        print("\nCOMPUTADOR VENCEU.")

    else:
        print("\nOpção inválida.")

elif computador == 1:
    
    if jogador == 0:
        print("\nCOMPUTADOR VENCEU.")
    elif jogador == 1:
        print("\nEMPATE.")
    elif jogador == 2:
        print("\nJOGADOR VENCEU.")
    else:
        print("\nOpção Inválida.")

elif computador == 2:

    if jogador == 0:
        print("\nJOGADOR VENCEU.")
    if jogador == 1:
        print("\nCOMPUTADOR VENCEU.")
    if jogador == 2:
        print("\nEMPATE.")
    else:
        print("\nOpção Inválida.")

#Game Over.