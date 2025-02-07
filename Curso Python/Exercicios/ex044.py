#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento. 
#A vista/cheque: 10% de desconto. A vista no cartão: 5% de desconto. 2x no cartão: preço normal. 3x ou mais no cartão 20% de juros.
print("=-=-=" * 10)
print("Lojas Silva.")
print("=-=-=" * 10)

preço = float(input("Digite o preço do produto: "))

print("""\nFORMAS DE PAGAMENTO
[1] à vista dinheiro ou cheque.
[2] à vista no cartão.
[3] 2x no cartão.
[4] 3x ou mais no cartão. """)

opcao = int(input("Digite a forma de pagamento desejada: "))

if opcao == 1:
    valor = preço - ((10/100) * preço)
    print(f"O valor do produto com 10% de desconto é R$ {valor:.2f}")
elif opcao == 2:
    valor = preço - ((5/100) * preço)
    print(f"O valor do produto com 5% de desconto é R${valor:.2f}")
elif opcao == 3:
    print(f"O produto não terá desconto, valor total: R${preço:.2f}")
elif opcao == 4:
    parcelas = int(input("Digite a quantidade de parcelas: "))
    juros = ((20/100) * preço)
    valor_total = preço + juros
    valor_parcela = valor_total / parcelas
    print(f"\nO valor das parcelas com 20% de juros: R${valor_parcela:.2f}, você pagará no total: R${valor_total:.2f}")

#Acabou.