nome = str(input("Qual é seu nome? "))

if nome == "Luis":
    print("Que bonito nome você tem!")
elif nome == "Pedro" or nome == "Guilherme" or nome == "Diego":
    print("Seu nome é bem popular no brasil")
elif nome in "Jéssica, Maria, Rosa, Barbara":
    print("Belo nome femenino")
else:
    print("Seu nome é bem normal!")

print("Tenha um bom dia.")

#Neste exemplo de algoritmo realizamos uma condição aninhada e nela foram feitas várias verificações.
