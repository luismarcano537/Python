#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todoas as informações possíveis sobre ele.

#Coletar dado pelo teclado.
dado = input('Digite alguma coisa: ')

#Mostrar tipo de dado ou tipo primitivo. 
print(type(dado))

#Verificações das informações. 
print(f'O dado é Alfabetico?: {dado.isalpha()}')
print(f'O Dado é Alfanumérico?: {dado.isalnum()}')
print(f'O dado está em Maiusculas?: {dado.isupper()}')

#Fim do programa.