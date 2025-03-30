import math

## Variaveis
a = int (input(f'Valor cateto a: '))
b = int (input(f'Valor cateto b: '))

## Contas
hipotenusa = math.sqrt(a**2 + b**2)
print (f'O resultado da Hipotenusa é {hipotenusa}')
