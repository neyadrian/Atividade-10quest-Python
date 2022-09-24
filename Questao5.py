print('Digite a seguir 3 números em ordem crescente e 1 aleatório')
n1 = int(input("Digite um primeiro número: "))
n2 = int(input("Digite um segundo número: "))
n3 = int(input("Digite um terceiro número: "))
n4 = int(input("Digite um quarto número diferente dos 3 primeiros: "))

if n4 > n3:
    print(f'A ordem decrescente dos números é: {n1},{n2},{n3} e {n4} ')

if n4 > n2 and n3 > n4:
    print(f'A ordem decrescente dos números é: {n3},{n4},{n2} e {n1} ')

if n4 > n1 and n2 > n4:
    print(f'A ordem decrescente dos números é: {n4},{n2},{n3} e {n1} ')

if n4 > n1:
    print(f'A ordem decrescente dos números é: {n3},{n2},{n1} e {n4} ')


    