'''Crie um programa que leia o nome e o preço de vários produtos produtos. 
O programa deverá perguntar se o usuário vai continuar. no final mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1000,00
c) Qual o nome do produto mais barato.'''
total = 0
produtos_acima_1000 = 0
produtos = 0
contador = 0
menor_preço = 0
barato = " "

print("=-=-=" * 10)
print("Loja Baratinha")
print("=-=-=" * 10)

while True:
    produto = str(input("\nQual o nome do produto: ")).strip().upper()
    preço = float(input(f"Digite o valor de {produto}: R$ "))
    total += preço
    produtos += 1
    contador += 1

    if preço >= 1000:
        produtos_acima_1000 += 1

    if contador == 1 or preço < menor_preço:
        menor_preço = preço
        barato = produto

    opção = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]

    while opção not in "SsNn":
        opção = str(input("\nOpção inválida! Deseja continuar? [S/N]: ")).strip().upper()[0]
    
    if opção in "Nn":
        print("\nEncerrando programa...")
        break

print(f"\nForam cadastrados um total de {produtos}.")
print(f"O total gasto na compra foi R$ {total:.2f}.")
print(f"{produtos_acima_1000} produtos tiveram um valor maior do que R$ 1000,00")
print(f"O produto {barato} foi o mais barato e custa R$ {menor_preço:.2f}")
