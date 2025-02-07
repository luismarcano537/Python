"""Faça uma tupla preenchida com os  20 primeiros colocados da tabela do campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os ultimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time Juventude(Originalmente era chapecoense, mas como no 2025 não está na lista alterei).""" 

times = ("Atletico-MG", "Bahia", "Botafogo", "Ceara", "Corinthians", "Cruzeiro", "Flamengo",
         "Fluminense", "Fortaleza", "Juventude", "Gremio", "Internacional", "Mirassol", "Palmeiras",
         "RB Bragantino", "Santos", "Sao Paulo", "Sport", "Vasco", "Vitoria")

print("=-=-=" * 10)
print("Placar de times Brasileirão")
print("=-=-=" * 10)

print(f"\nOs primeiros 5 times no placar: {times[0:5]}")
print(f"Os ultimos 4 times no placar: {times[-4:]}")
print(f"Os times em ordem alfabético: {sorted(times)}")
print(f"O time juventude está na posição: {times.index("Juventude")}")
