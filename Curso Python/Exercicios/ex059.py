#Crie um programa que leia dois valores e mostre um menu na tela: 
# [1] Somar [2] Multiplicar [3] Maior [4] Novos números. [5] Sair do programa. 
# Seu programa deverá realizar a operação solicitada de cada caso.
print("\nMe informe dois valores ou mais e escolha uma opção!")
n1 = int(input("\nDigite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opcao = 0

print(""""Escolha uma opção:
      [1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Novos números
      [5] Sair do programa""")

while opcao != 5:
    try:
        opcao = int(input("Digite uma opção (Apenas números): "))

        if opcao == 1:
            soma = n1 + n2
            print(f"A soma entre {n1} e {n2} é {soma}")
        elif opcao == 2:
            multiplicacao = n1 * n2
            print(f"A multiplicação de {n1} X {n2}: {multiplicacao}")
        elif opcao == 3:
            if n1 > n2:
                print(f"{n1} é maior que {n2}")
            elif n2 > n1:
                print(f"{n2} é maior que {n1}")
            else:
                print(f"{n1} e {n2} são iguais.")
        elif opcao == 4:
            print(f"Informe os novos números!")
            n1 = int(input("Digite o primeiro valor: "))
            n2 = int(input("Digite o segundo valor: "))
        elif opcao == 5:
            print("Você escolheu sair do programa, até mais!\n")
    except ValueError:
        print("Opção inválida! Digite novamente (Apenas números)")
