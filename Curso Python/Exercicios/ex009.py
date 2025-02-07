#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada. 
num = int(input('Me diga um número para ver sua tabuada: '))

#Mostrar tabuada
print('-' * 12)
print('{} X {:2} = {}'.format(num, 1, num*1))
print('{} X {:2} = {}'.format(num, 2, num*2))
print('{} X {:2} = {}'.format(num, 3, num*3))
print('{} X {:2} = {}'.format(num, 4, num*4))
print('{} X {:2} = {}'.format(num, 5, num*5))
print('{} X {:2} = {}'.format(num, 6, num*6))
print('{} X {:2} = {}'.format(num, 7, num*7))
print('{} X {:2} = {}'.format(num, 8, num*8))
print('{} X {:2} = {}'.format(num, 9, num*9))
print('{} X {:2} = {}'.format(num, 10, num*10))
print('-' * 12)

print('\nAgora você tem a tabuada de {}, acabou'.format(num))

#Acabou. 