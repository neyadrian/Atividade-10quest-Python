print('Menu de Opções:')
print('    1. Somar dois números')
print('    2. Raíz quadrada de um número')
op = int(input('Digite a opção desejada: '))

if op == 1:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

    result = n1 + n2
    print(f'O resultado da sua soma foi: {result} ')

import math
if op == 2:
    num = int(input('Digite um número: '))

    print(f'A raíz quadrada do seu número é: {math.sqrt(num)} ')




