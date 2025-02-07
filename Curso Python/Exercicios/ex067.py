print("=-=-=" * 10)
print("Tabuada V3")
print("=-=-=" * 10)
while True:
    num = int(input("\nDigite um número e lhe darei sua tabuada (Ou digite um número negativo para encerrar): "))
    if num < 0:
        break
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
print("\nPrograma de tabuadas encerrado.\n")
