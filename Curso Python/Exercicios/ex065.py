#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre
# a média entre todos os valores e qual foi o maior e o menos valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print("Digite os números desejados, calcularemos sua media e o maior, menor entre eles.")
opcao = "Ss"
num = 0
soma = 0
contador = 0
maior = None
menor = None

while opcao in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    contador += 1
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num    
    opcao = str(input("Deseja continua? [S/N]: ")).strip().upper()

media = soma /  contador
print(f"""  Foram informados {contador} números, a soma entre eles foi {soma} e a média foi {media}
O maior número foi {maior} e o menor número foi {menor}""")
