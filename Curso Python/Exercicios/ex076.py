"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequeência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""
produtos = ("Caderno", 4.99, "Lapiz", 1.75, "Borracha", 3.99, "Mochila", 139.45, "Estojo", 15.99, "Caneta", 4.99)

print("=" * 40)
print(f"{"Listagem de Produtos":^30}")
print("=" * 40)

for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f"{produtos[p]:.<30}", end="")
    else:
        print(f"R$ {produtos[p]:>7}")
print("=" * 40)
