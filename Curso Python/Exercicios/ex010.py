#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
nome = input('Me diga se nome: ')
dinheiro = float(input('Quanto dinheiro você tem disponível?: R$'))
dolar = 5.69
disponível = dinheiro / dolar

#Mostrar as informações. 
print('\n{}, você possui R${} e pode comprar USD{:.2f}'.format(nome, dinheiro, disponível))

#Acabou. 