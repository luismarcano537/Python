#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu índice de massa corporal (IMC) e mostre seu status, de acordo com a tabela abaixo.
#IMC abaixo de 18,5: Abaixo do peso. Entre 18,5 e 25: Peso ideal. 25 até 30: Sobrepeso. 30 até 40: Obesidade. Acima de 40: Obesidade mórbida. 
print("=-=-=-=" * 20)
print("Medidor de IMC!")
print("=-=-=-=" * 20)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = float(peso / (altura * altura))

if imc <18.5:
    print(f"\nSeu IMC é {imc:.2f}, você está abaixo do peso.\n")
elif imc < 25:
    print(f"\nSeu IMC é {imc:.2f}, você está no peso ideal.\n")
elif imc <30:
    print(f"\nSeu IMC é {imc:.2f}, você está com sobrepeso.\n")
else:
    print(f"Seu IMC é {imc:.2f}, você está com obesidade mórbida.\n")

#Acabou.