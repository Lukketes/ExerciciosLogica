def eh_par(valor):
    return valor % 2 == 0
    
# Algoritmo para descobrir se é par.
valor = int(input("Escreva o Valor: "))
if eh_par(valor):
    print("É par")
else:
    print("É ímpar")