#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. (após a sopa, a sacada da casa, a torre da derrota, 
# o lobo  ama o bolo, anotaram a data da maratona). 
frase = str(input("\nDigite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f"O inverso da frase: {frase} é {inverso}")

if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
