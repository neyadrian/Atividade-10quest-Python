
note1 = float(input('Digite a 1ª média: '))
note2 = float(input('Digite a 2ª média: '))
note3 = float(input('Digite a 3ª média: '))

media = (note1 + note2 + note3) / 3
exame = 6 - media

if media < 3:
    print('REPROVADO')
elif media >= 3 and media < 6:
    print(f'Fará um EXAME, presisa de {exame} para ser APROVADO')
elif media >= 6:
    print('APROVADO')

elif media >= 7:
    print('APROVADO')
