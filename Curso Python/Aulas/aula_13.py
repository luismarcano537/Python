print("\nSem iteração:")
print("oi")
print("oi")
print("oi")
print("oi")

print("\nAgora com laço:")
for c in range(1, 6): #Aqui irá realizar 5 prints, porque estamos desconsiderando o 0, mas se quiser 6 pode substituir o 1 por 0.
    print("oi")
print("\nFIM")

#Outro exemplo.
for c in range(6, 0, -1): #Conta de forma invertida, ou seja de 6 para 0. O -1 subtrai.
    print(c)
print("\nFim")

#Se quisermos realizar uma iteração com base em um dado inserido pelo usuário:
n = int(input("\nDigite um número: "))
for c in range(0, n+1): #Adicionamos +1, pois se o usuário quiser 10, ele entregará 9 devido a indentação. 
    print(c)
print("FIM")

#Caso queira com "pulo" a contagem:
i = int(input("\nInsira o inicio: "))
f = int(input("Insira o fim: "))
p = int(input("Insira o passo: ")) #Terá a função de informar como deve contar os números.
for c in range(i, f+1, p):
    print(c)
print("FIM\n")

#Imagine que precise de obter os números dados pelo usuário e realizar a somatoria entre eles. 
s = 0
for c in range(0, 4):
    n = int(input("Digite um número: "))
    s += n
print(f"O soma de todos os valores é: {s}\n")
