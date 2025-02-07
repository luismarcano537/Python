#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. 
#Identificando o usuário e coletando dados. 
nome = input('Seja bem-vindo! digite seu nome: ')
idade = (input('Qual a sua idade: '))
cor = input('Digite sua cor favorita: ')
comida = input('Digite sua comida favorita: ')
numero = (input(f'{nome}, por ultimo... Me diga qual o seu número favorito.'))

#Imprimir dados na tela. 
print('\nMuito obrigado por preencher as informções')
print(f'Seu nome é {nome}, sua idade é {idade}, sua cor favorita é {cor}, a comida que você mais gosta é: {comida} e seu número favorito é {numero}')

#Mostrando os tipos de dados e algumas informações. 
print('\nQual tipo de primitivo é seu nome?: ', type(nome))
print('Sua idade é um número: ', idade.isnumeric())
print('Sua cor favorita é alfabetica?: ', cor.isalpha())
print('Sua comida favorita é um número?: ', comida.isnumeric())
print('Seu número tem um espaço?: ', numero.isspace())

print(f'\n{nome}, Obrigado por ter utilizado nosso programa.')