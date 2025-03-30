# Variaveis
Valor1 = int(input(f'Digite o valor 1: '))
Valor2 = int(input(f'Digite o valor 2: '))
Valor3 = int(input(f'Digite o valor 3: '))
soma = int

#Condição
if Valor1 < 0 or Valor2 < 0 or Valor3 < 0:
    print("Erro: número negativo")

# Conta
soma = Valor1 + Valor2 + Valor3
media = soma / 3
if media > 7:
    print(f'Aprovado')
if media < 7:
    print(f'Reprovado')
