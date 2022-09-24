note1 = float(input('Digite a nota do Trab. de Laboratório: '))
note2 = float(input('Digite a nota da Av. Semestral: '))
note3 = float(input('Digite a nota do Exame Final: '))

media = ((note1 * 2) + (note2 * 3) + (note3 * 5)) / 10

if media < 5:
    print('Conceito E')
else:
    if media < 6:
        print('Conceito D')
    else:
        if media < 7:
            print('Conceito C')
        else:
            if media < 8:
                print('Conceito B')
            else:
                print('Conceito A')
