"""teste = list()
teste.append("Gustavo")
teste.append("40")
galera = list()
galera.append(teste[:]) #Copia a estrutura da lista teste.
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera) #Imprime "Gustavo", 40"""

#Outra forma de declarar a lista galera (Estrutura)
#galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]

"""for pessoa in galera:
    print(f"{pessoa}... ", end="")"""

"""print(galera[0][1])"""

#for p in galera:
 #   print(f"{p[0]} tem {p[1]} anos de idade.")

galera = list()
dado = list()
totmaior = 0
totmin = 0

for c in range(0, 3):
	dado.append(str(input(f"Nome da {c+1}ª pessoa: ")))
	dado.append(int(input("Idade: ")))
	galera.append(dado[:])
	dado.clear() #excluir apenas quando for uma copia, se não for copia e estiver ligado, ao excluir irá armazenar listas vazias.
	
for p in galera:
	print(f"{p[0]} tem {p[1]} anos de idade.")

for p in galera:
	if p[1] > 21:
		print(f"{p[0]} é maior de idade.")
		totmaior += 1
	else:
		print(f"{p[0]} é menor de idade.")
		totmin += 1
		
print(f"Temos um total de {totmaior} pessoas maior de idade e {totmin} menores de idade.")
