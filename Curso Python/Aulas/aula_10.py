#Faça um programa que leia 4 notas do aluno e informe a média e se ele está aprovado ou reprovado. 
print("\nSeja bem-vindo, caro aluno. \nVamos verificar se foi aprovado.")
nome = input("Por favor, digite seu nome: ")

n1 = float(input("\nDigite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

#Calcular a média:
media = ((n1 + n2 + n3 + n4) / 4) #Utilizamos os parenteses para alterar a ordem de precedencia. 

#Verificar se o aluno foi aprovado ou não: 
if media >= 5.0:
    print(f"\n{nome}, Você foi aprovado, parabéns")

else:
    print(f"{nome}, Você foi reprovado, estude mais.")

print("\nObrigado por ter utilizado o nosso algoritmo de verificação.\n")

#acabou, seu burro. 