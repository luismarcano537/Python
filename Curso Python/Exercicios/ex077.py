"""Crie um programa que tenha uma tupla com várias palavras(Sem acentos). Depois disso,
Você deve mostrar, para cada palavra, quais são as suas vogais."""

palavras = ("Casa", "Carro", "Macaco", "Mochila", "Moto", "Moveis", "Geladeira")

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos as vogais: ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
        