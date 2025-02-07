#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
# 1 para binário, 2 para octal e 3 para hexadecimal.
import time as tm

print("=-=-=" *10)
print("Seja bem-vindo ao conversor de números inteiros.")
print("=-=-=" * 10)

num = int(input("\nDigite um número inteiro: "))

print('''\nDigite a opção desejada: 
      [1] para binário.
      [2] para octal.
      [3] para hexadecimal.
      [0] para sair''')

opcao = int(input("\nDigite sua opção: "))

if opcao == 1:
    print(f"O número {num} convertido em binário é {bin(num)[2:]}")
elif opcao == 2:
    print(f"O número {num} convertido para octal é {oct(num)[2:]}")
elif opcao == 3:
    print(f"O número {num} convertido para hexadecimal {hex(num)[2:]}")
elif opcao == 0:
    print("Sistema sendo encerrado!")
else:
    print("Digite um número válido.")

tm.sleep(2)
print("\nObrigado por ter utilizado o sistema de conversão de inteiros.\n")
