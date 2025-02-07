#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. 

#Coletar dados. 
n = int(input('Digite um número da sua preferencia: '))

print('O número que você digitou é: {}'.format(n))
print('O dobro desse número é: {}'.format(n * 2))
print('O triplo desse número é: {}'.format(n * 3))
print('A raiz quadrada desse número é: {:.2f}'.format(n ** (1/2)))

print('\nAcabou')
