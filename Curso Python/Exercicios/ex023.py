#Faça um programa que leia um número do 0 ao 9999 e mostre na tela cada um dos dígitos separados.
n = int(input("\nDigite um número: "))
u = (n // 1 % 10)
d = (n // 10 % 10)
c = (n // 100 % 10)
m = (n // 1000 % 10)
print(f"\nAnalisando o número {n}")

print(f"\nUnidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")

#Acabou.