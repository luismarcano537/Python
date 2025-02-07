#Desenvolva um programa que leia seis números inteiros e mostre a 
# soma apenas daqueles que forem pares. 
# Se o valor digitado for impar, desconsidere-o.
print("\nInforme seis números e retornarei com a soma dos números pares!\n")
soma = 0
for i in range(1, 7):
    num = int(input(f"Digite o {i}º número: "))
    if num % 2 == 0:
        soma += num

print(f"\nA soma dos números pares é: {soma}")
#Acabou. 