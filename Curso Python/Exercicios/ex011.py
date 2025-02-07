#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. 
#Sabendo que cada litro de tinta pinta uma área de 2mts quadrados. 

#Coletar informações. 
larg = float(input('Digite a largura da sua parede: '))
alt = float(input('Digite a altura da sua parede: '))
area = larg * alt
tinta = area / 2

#Mostrar informações processadas. 
print(f'\nA sua parede possui: {area}m²')
print(f'No entanto, você precisará de {tinta} lts para pintar sua parede.')

print('\nEspero que tenha lhe ajudado!')
