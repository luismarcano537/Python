#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um 
# atleta e mostre sua categoria, de acordo com sua idade. Até 9 anos: Mirim. Até 14 anos: Infantil. 
# Até 19 anos: Júnior. Acima de 25 anos: MASTER.

nome = input("\nDigite o nome do atleta: ")
ano = int(input("Digite o ano de nascimento: "))
idade = int( 2024 - ano)

#Condição de idade para verificar a classificação do atleta. 

if idade <= 9:
    print(f"\nQume nasceu em {ano} tem {idade} anos.")
    print(f"{nome}, é MIRIM.\n")
elif 9 <= idade <= 14:
    print(f"\nQuem nasceu em {ano} tem {idade} anos.")
    print(f"{nome}, é INFANTIL.\n")
elif 14 <= idade <= 19:
    print(f"\nQuem nasceu em {ano} tem {idade} anos.")
    print(f"{nome}, é JUNIOR.\n")
elif 19 <= idade <= 25:
    print(f"\nQuem nasceu em {ano} tem {idade} anos.")
    print(f"{nome}, é SÊNIOR.\n")
elif idade >= 25:
    print(f"\nQuem nasceu em {ano} tem {idade} anos.")
    print(f"{nome}, Você é MASTER.\n")
else:
    print("\nAtenção: ERROR!")
    print("Não existe idade de número negativo, insira novamente.\n")
