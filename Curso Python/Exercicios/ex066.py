cont = 0
soma = 0
while True:
    n = int(input("Digite um número: (Ou 999 para parar)"))
    if n == 999:
        break
    soma += n
    cont += 1

print(f"Foram informados {cont} números, a soma total deles é {soma}")
