#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. 

#Coletar informações.
print('\nOlá, seja bem-vindo. Eu estare lhe entregando o valor do produto com 5% Off!')
produto = float(input('me diga o valor do produto: R$ '))
desconto = (produto * 5 /100)
valor_final = produto - desconto


print(f'Caro cliente, o produto que você informou tem o valor de R$ {produto:.2f}')
print(f'Você ganhou 5% off na sua compra.')
print(f'Valor a pagar: R${valor_final:.2f}')

print('Acabou')