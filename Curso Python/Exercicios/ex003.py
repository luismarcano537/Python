#Crie um programa que leia dois números e mostre a soma entre eles. 
nome = input('Digite seu nome: ')
print(f'{nome}, lhe estarei ajudando para realizar a soma entre dois números.')

#Declaração dos valores.
number_01 = float(input('Digite um número: ')) #Podemos utilizar float ou int dependendo o contexto do uso.
number_02 = float(input('Digite outro número: ')) #Podemos utilizar float ou int dependendo o contexto do uso.

#Soma dos valores. 
resultado = (float(number_01)) + (float(number_02))

#exibir resultado. 
print(f'{nome}, A soma entre o valor {number_01} e {number_02} é: {resultado}')

print('Obrigado por ter utilizado o programa de soma de valores!')
