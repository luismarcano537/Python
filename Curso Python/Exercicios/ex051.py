#Desenvolva um programa que leia o primeiro termo e a razão 
#de uma PA. No final, mostre os 10 primeiros termos dessa 
# progressão. (Progressão aritmética). 
print("=-=-=-=" * 10)
print("10 Primeiros termos de uma PA")
print("=-=-=-=" * 10)

termo_1 = int(input("\nDigite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = termo_1 + 10 * razao

for i in range(termo_1, decimo, razao):
    print(f"{i}", end= " -> ")
print("Acabou.\n")

#Acabou.