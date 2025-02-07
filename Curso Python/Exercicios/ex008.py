#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. 
nome = input('Seja bem-vindo, me diga seu nome: ')
metros = float(input('Me diga uma distância em metros: '))
cm = float(metros) * 100
mm = float(metros) * 1000

#Mostrar dados. 
print('{}, A distância que você me informou é: {}, a distância em centímetros é: {:.0f}cm e adistância em milímetros é: {:.0f}mm'.format(nome, metros, cm, mm))

#Acabou. 
print('Acabou!')