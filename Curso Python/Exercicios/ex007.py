#Desenvolva um programa que leia as duas notas de um aluno e calcule e mostre a sua média. 
nome = input('Seja bem vindo, me diga por favor seu nome: ')
n1 = float(input('{}, Me diga sua primeira nota: '.format(nome)))
n2 = float(input('Me diga sua segunda nota: '))
m = (float(n1) + float(n2)) / 2

#Informar o resultado. 
print('{}, o total das suas notas foi: {}, e a sua nota média foi: {}'.format(nome, float(n1) + float(n2), m))
print('\nAcabou!')
