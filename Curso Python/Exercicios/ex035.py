#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 
print("=-=" * 20)
print("Vamos analisar um triângulo.")
print("=-=" * 20)

a = float(input("\nDigite o cumprimento da primeira reta: "))
b = float(input("Digite o cumprimento da segunda reta: "))
c = float(input("Digite o cumprimento da terceira reta: "))

#Verificar se pode ser formado um triângulo.
if a < b + c and b < a + c and c < a + b:
    print("\nOs segmentos podem formar um triângulo.")
else:
    print("Os segmentos não podem formar um triângulo.")
    