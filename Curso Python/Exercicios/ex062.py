#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print("Gerador de PA")
print("=-=" * 10)
primeiro = int(input("Digite o primeiro termo: "))
Razão = int(input("Digite a Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} -> ", end= " ")
        termo += Razão
        cont += 1
    mais = int(input("\nQuantos termos a mais você quer mostrar?: "))
print(f"Progressão encerrada, foram mostrados um total de {total} termos.")
