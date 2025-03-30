import math

#Variaveis
a = float(input("Digite o Valor de A: "))
b = float(input("Digite o Valor de B: "))
c = float(input("Digite o Valor de C: "))

#Verificação se a = 0
if a == 0:
    print("Não existe raiz de 0!")

else:
    delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("Não há raizes reais")

elif delta == 0:
    x = -b / (2 * a)
    print("A equação possui apenas uma raiz real: {x}")

elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"A equação possui duas raizes reais: x1 = {x1}, x2 = {x2}")

