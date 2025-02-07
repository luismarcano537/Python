#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado. 

#Coletar informações. 
print('\nOlá, seja bem vindo! Lhe estarei informando quanto deve pagar pelo carro alugado.')
km = float(input('Quantos Kilometros você rodou no carro?: '))
dias = int(input('Digite por quantos dias você utilizou o carro: '))
valor_dias = dias * 60
valor_km = km * 0.15
total = valor_dias + valor_km

#Mostrar informações. 
print(f'Você utilizou por {dias} dias e percorreu {km}km!')
print(f'Você deve pagar R${valor_dias} pelos dias com o carro e deve pagar R${valor_km} pelos KM percorridos!')
print(f'Valor a pagar: R${total}')
print('Até mais.')

#Acabou.