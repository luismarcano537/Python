#Faça um programa que calcule a soma entre todos os números ímpares que são 
# multiplos de três e que se encontram no intervalo de 1 até 200.
print("=-=-=" * 10)
print("Vamos calcular a soma de todos os números ímpares múltiplos de três de 1 até o 500.")
print("=-=-=" * 10)

soma = 0 #Aplicação de variável acumuladora.
cont = 0 #Aplicação de variável contadora. 

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0: #Verificamos se o número é ímpar e se é divisivel por 3.
        soma += i
        cont += 1
        #print(f"O número: {i} é divisivel por 3.") #Para economizar memória, não irei utilizar este comando, pois não é eficiente.

print(f"\nA Soma total dos {cont} números divisiveis por 3 é: {soma}\n")
#Acabou. 