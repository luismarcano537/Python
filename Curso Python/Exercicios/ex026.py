#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra A.
#Informe em que posição aparece por primeira vez e em que posição ela aparece na ultima vez. 

frase = str(input("Digite uma frase: ")).strip().upper()
print(f"\n Você disse a frase: {frase}")

print(f"A frase possui a letra 'a' {frase.count('A')} vezes!")
print(f"A letra 'A' aparece por primeira vez na {frase.find('A') +1} posição.")
print(f"A letra 'A' aparece na ultima vez na {frase.rfind('A') +1} posição.\n")

#Acabou meu lindo. 