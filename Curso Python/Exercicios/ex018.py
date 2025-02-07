#Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.
import math

angl = float(input("Digite o valor do ângulo: "))
angl_rad = math.radians(angl) #Utilizamos a função math para converter o valor do angulo para radiano.
seno = math.sin(angl_rad) #também podemos utilizar: math.sin(math.rad(angl)).
cosseno = math.cos(angl_rad)
tangente = math.tan(angl_rad)

print(f"O valor do angulo é {angl:.2f}, \nO valor do Seno é {seno:.2f}, \nO valor do cosseno é {cosseno:.2f},")
print(f"O valor da tangente é {tangente:.2f}")

#Acabou. 