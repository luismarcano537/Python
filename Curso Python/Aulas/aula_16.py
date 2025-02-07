#Tuplas devem ser iniciadas com parenteses.
lanche = ("Hamburguer", "Suco", "Pizza", "Pudin") #A partir do Python 3.5 não é necessário colocar parenteses.

print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-3:])

#Tuplas são imutáveis.
lanche[1] = ("Refrigerante") #Ao executar irá informar erro. 

#Se quisermos acessar a todos os valores armazenados na tupla, podemos fazer:
for i in lanche:
    print(f"Vou comer {i}")
print("Comi pra caramba!")

#Outra forma de utilizar um for com tuplas seria:
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")
print("Comi pra caramba")

#Se você precisar de informar a localização do valor na tupla, podemos utilizar:

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} em {cont}")
print("\nComi pra caramba!") 

#Outra forma de informar a posição do valor na tupla é:
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

#Para organizar uma tupla, podemos utilizar a função sorted:
print(sorted(lanche)) #Apenas organiza, mas não altera o valor.

#Se precisarmos juntas os valores de tuplas, podemos realizar: 
a = (2, 4, 6)
b = (8, 9, 12, 4)
c = a + b 
print(len(c))
print(c.count(5)) #Cuenta quantas vezes está aparecendo o 5 em c.
print(c)
print(c.index(8)) #Informa a posição de 8, ou seja, index informa a indetação.

#Tuplas no Python aceitam diversos tipos de dados, int, strings, floats, são como vetores em C ou java.
pessoa = ("Gustavo", 39, "M", 99.88)
del(pessoa) #Tuplas são imutáveis, porém, você pode apagar elas. 
print(pessoa) 
