#Desenvolva um programa que pergunte a distância de uma viagem em KM. 
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas. 
print("=-=" * 15)
print("Seja bem-vindo, vamos simular o preço da viagem até a cidade que você deseja conhecer!")
print("=-=" * 15)

cidade = str(input("\nDigite o nome de cidade que você deseja conhecer: ")).strip()

distancia = float(input("Digite a distância em KM: "))

#Calcular o preço a través de condicionais. 
if distancia <= 200:
    preco = float(distancia * 0.50)
    print(f"\nA viagem até {cidade} possuí {distancia}km, o valor da sua viagem é R${preco:.2f}")
else:
    preco = float(distancia * 0.45)
    print(f"\nA viagem até {cidade} possui {distancia}km, o valor da sua viagem é R${preco:.2f}")

print("=-=" * 15)
print("Obrigado por ter utilizado o nosso algoritmo.")
print("=-=" * 15)
