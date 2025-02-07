#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar os 80Km/h, será multado. 
#Multa é de R$ 7.00 por cada km/h, informe o valor da multa.
velocidade = float(input("Digite a velocidade em KM/h: "))

if velocidade > 80:
    print("Opa, você foi multado.")
    print(f"O valor a pagar é: R${(velocidade - 80) * 7.0:.2f}")
else:
    print("Você não foi multado, dirija com segurança.")
    