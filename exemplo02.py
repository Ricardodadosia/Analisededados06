resposta = 'S'
while resposta == 'S':
    numero = int(input('informe um número: '))

    dobro = numero * 2 
    triplo = numero * 3
    quadradro = numero ** 2

    print(f'dobro: {dobro}')
    print(f'triplo: {triplo}')
    print(f'quadrado: {quadradro}')

    resposta = input('quer continuar: [S/N]').upper()