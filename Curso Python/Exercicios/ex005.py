#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor. 
n1 = int(input("Digite um número inteiro: "))
n2 = int(1)

#Manipulação da informação para entregar o resultado. 
n_sucessor = int(n1) + int(n2)
n_antecessor = int(n1) - int(n2)

#Informar resultado. 
print('O número que você digitou é: {}, por tanto, o atencessor é: {}, e o sucessor é: {}'.format(n1, n_antecessor, n_sucessor))
print('Acabou')

#Fim do código. 

#Outra forma de elaborar o código. (Forma feita pelo guanabara).
n = int(input('Digite um número: '))

print('Analisando o número que você digitou ({}), seu antecessor é: {}, e seu sucessor é: {}'.format(n, n - 1, n + 1))