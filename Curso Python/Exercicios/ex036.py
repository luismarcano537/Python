#Escreva um programa para aprovar um emprestimo bancário para a compra de uma csa. 
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder o 30% do salário ou então será negado o emprestimo.
import time as tm

print("=-=-=" *10)
print("Seja bem-vindo ao sistema de calculo de emprestimo!")
print("=-=-=" *10)

#Coletar informações.
nome = str(input("Digite seu nome, por favor: "))
idade = int(input(f"{nome}, informe sua idade: "))
salario = float(input("Digite seu salário mensal: "))
valor_casa = float(input("Digite o valor da casa: R$ "))
tempo_anos = int(input("Em quantos anos, deseja pagar? "))


print("=-=-=" *10)
print("Analisando suas informações...")
tm.sleep(3)
print("=-=-=\n" *10)

print("Resultado exemplo")

#Calculo das informações.
qtde_parcelas = int(tempo_anos * 12)
valor_parcelas = float(valor_casa / qtde_parcelas)
orçamento_dpnvl = float(salario *30 /100)

#Verificar informações.
if valor_parcelas > orçamento_dpnvl and idade < 18:
    print(f"{nome}, Pedimos desculpa, após análises, o crédito não foi aprovado.")
else:
    print(f"{nome}, Parabéns, seu crédito imobiliario foi aprovado.\n")
    print(f"Quantidade de parcelas: {qtde_parcelas}")
    print(f"Valor de cada parcela: R$ {valor_parcelas:.2f}")
    print(f"Duração do emprestimo: {tempo_anos} anos.")

print("=-=-=" *10)
print("Obrigado por ter utilizado nosso sistema!")
print("=-=-=" *10)

#Acabou. 