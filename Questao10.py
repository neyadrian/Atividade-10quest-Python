print('Primeira Data')
dia1 = int(input('Digite o dia (1 a 31): '))
mes1 = int(input('Digite o mês (1 a 12): '))
ano1 = int(input('Digite o ano: '))

print('Segunda Data')
dia2 = int(input('Digite o dia (1 a 31): '))
mes2 = int(input('Digite o mês (1 a 12): '))
ano2 = int(input('Digite o ano: '))

#Comparativo de Anos
if ano1 > ano2:
        print(f'A maior data é {dia1}/{mes1}/{ano1}')
elif ano2 > ano1:
        print(f'A maior data é {dia2}/{mes2}/{ano2}')

#Comparativo de Meses
if mes1 > mes2:
    if ano1 > ano2:
        print(f'A maior data é {dia1}/{mes1}/{ano1}')
    elif ano2 > ano1:
        print(f'A maior data é {dia2}/{mes2}/{ano2}')

elif mes2 > mes1:
    if ano1 > ano2:
        print(f'A maior data é {dia1}/{mes1}/{ano1}')
    elif ano2 > ano1:
        print(f'A maior data é {dia2}/{mes2}/{ano2}')

#Comparativo de dias
if dia1> dia2:
    if ano1 > ano2:
        print(f'A maior data é {dia1}/{mes1}/{ano1}')
    elif ano2 > ano1:    
        print(f'A maior data é {dia1}/{mes1}/{ano2}')

elif dia2 > dia1:
    if ano1 > ano2:
        print(f'A maior data é {dia2}/{mes1}/{ano1}')
        
    elif ano2 > ano1:
        print(f'A maior data é {dia2}/{mes2}/{ano2}')
        