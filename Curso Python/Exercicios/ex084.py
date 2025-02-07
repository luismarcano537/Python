pessoas = list()
dados = list()
cont = 0

while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    cont += 1

    opcao = (str(input("Deseja continuar? [S/N]: "))).upper()
    if opcao in "N":
        print("Encerrando programa...")
        break
    