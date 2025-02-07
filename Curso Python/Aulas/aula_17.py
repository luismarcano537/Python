#num = (2, 5, 9, 1)
#num[2] = 3 O Python não aceita alterar uma tupla, porém, podemos criar uma lista.
#numeros = [1, 3, 5, 8]
#numeros[2] = 6

#print(numeros)

"""numeros.append(7) #Adiciona no final da lista. 
numeros.sort() #Organiza os valores.
numeros.sort(reverse=True) #Organiza invertidamente os números.
numeros.insert(2, 0) #Na posição 2 irá colocar o número 0, porém, apenas cria um novo espaço, não faz o delete do item que estava na posição anteriormente."""
"""print(numeros)
print(f"A lista números, tem um total de {len(numeros)} números.")"""
#umeros.pop(2) #Remove o elemento informado no parametro(lembrando que é o valor na posição.)
#numeros.remove(2) Procura na lista o valor 2 e realiza o delete, caso tenha mais de um, ele irá apenas remover o primeiro a encontrar. 

"""valores = [] #Podemos também criar a lista: valores = list()
valores.append(5)
valores.append(4)
valores.append(3)
valores.append(2)
valores.append(1)"""

"""for v in valores:
    print(f"{v}...", end=" ")"""

"""for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista!")

#Outra forma de inserir valores na lista de forma automatizada é.
for cont in range(0, 5):
    valores.append(int(input("Digite um número: ")))

for v in valores:
    print(f"{v}...", end="")"""

"""a = [2, 7, 8]
b = a #Cria uma relação entre as duas listas, se um valor for alterado em B, também será em a. 
b[2] = 4
print(f"Lista A: {a}")
print(f"Lista B? {b}")"""

#Agora, da seguinte forma, ele não irá criar uma relação e sim uma copia.
a = [4, 7, 2]
b = a[:]
b[2] = 5
print(f"Lista A: {a}")
print(f"Lista B: {b}")
