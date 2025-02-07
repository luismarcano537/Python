#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
# Equilatero: Todos os lados iguais. Isósceles: Dois lados iguais, um diferente. Escaleno: Todos os lados diferentes.

print("=-=-=-=" * 20)
print("Vamos analisar um triângulo.")
print("=-=-=-=" * 20)

a = float(input("\nDigite o cumprimento da primeira reta: "))
b = float(input("Digite o cumprimento da segunda reta: "))
c = float(input("Digite o cumprimento da terceira reta: "))

#Verificar se pode ser formado um triângulo.
if a < b + c and b < a + c and c < a + b:
    print("\nOs segmentos podem formar um triângulo.")
    if a == b == c:
        print("\nO triângulo a ser formado é um EQUILÁTERO.\n")
    elif a != b != c != a:
        print("\nO triângulo a ser formado é um ESCALENO.\n")
    else:
        print("\nO triângulo a ser formado é um ISÓSCELES.\n")
else:
    print(f"\nOs segmentos não podem formar um triângulo.")

#Acabou.