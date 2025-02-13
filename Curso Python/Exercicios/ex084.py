import time
pessoas = list()
principal = list()
maiorpeso = 0
menorpeso = 0

while True:
    nome = str(input("\nDigite o nome: "))
    peso = float(input("Digite o peso: "))
    opcao = str(input("\nDeseja continuar? [S/N]: ")).upper().strip()

    pessoas.append(nome)
    pessoas.append(peso)

    if len(principal) == 0:
        maiorpeso = menorpeso = pessoas[1]
    else:
        if pessoas[1] > maiorpeso:
            maiorpeso = pessoas[1]
        if pessoas[1] < menorpeso:
            menorpeso = pessoas[1]

    principal.append(pessoas[:])
    pessoas.clear()

    if opcao in "Nn":
        print("Programa será encerrado...")
        time.sleep(2)
        print("\nPrograma encerrado.")
        break

print(f"Ao todo você cadastrou {len(principal)} pessoas.")
print(f"{maiorpeso}Kg foi o maior peso, sendo de: ", end="")
for p in principal:
    if p[1] == maiorpeso:
        print(f"[{p[0]}]  ", end="")
print()

print(f"{menorpeso}Kg foi o menor peso, sendo de: ", end="")
for p in principal:
    if p[1] == menorpeso:
        print(f"[{p[0]}]", end="")
print()
