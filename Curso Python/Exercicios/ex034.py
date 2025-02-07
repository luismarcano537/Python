#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. 
print("Vamos calcular o aumento do salário do funcionário.")

salario = float(input("Digite o salário do funcionário: R$ "))

#Realizar o calculo.
if salario > 1250:
    novo = (salario * 10 /100) + salario
else:
    novo = (salario * 15 /100) + salario

#Imprimir resultados.
print(f"\nO novo salário do funionário é: {novo:.2f}")
#acabou...