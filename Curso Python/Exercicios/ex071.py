"""Crie um programa que simule o funcionamento de um caixa eletrônico. 
No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o prorgama vai informar quantas cédulas de cada valor serão entregues.
Considere que o caixa possui cédulas de R$ 50, 20, 10, 1."""
print("=-=-=" * 10)
print("Caixa eletrônico")
print("=-=-=" * 10)

valor = int(input("Digite o valor a ser retirado: R$ "))
total = valor
cedula = 50
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} de R$ {cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0

        if total == 0:
            break

print("Encerrando caixa... Até mais.")
