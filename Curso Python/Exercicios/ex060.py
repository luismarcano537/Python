#Faça um programa que leia um número qualquer e mostre o seu fatorial. 
#Exemplo: 5! = 5*4*3*2*1 = 120.
print("=-=-=" * 10)
print("Calculo de fatorial")
print("=-=-=" * 10)

n1 = int(input("Digite um número para calcular seu fatorial: "))
c = n1
f = 1
print(f"Calculando {n1}! = ", end=" ")
while c > 0:
    print(c, end= " ")
    print(" X " if c > 1 else " = ", end=" ")
    f *= c
    c -= 1
print(f"{f}")
