#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher.
#Só que agora utilizando um laço for.
print("\nVamos verificar a tabuada do número que desejar!")
num = int(input("Digite um número e lhe darei sua tabuda: "))

print(f"\nTabuada de {num}: \n")
for i in range(1, 11):
    print(f"{num}  X {i}: {num * i}")


#Acabou. 