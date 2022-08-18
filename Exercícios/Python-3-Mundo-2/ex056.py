'''Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas. No final do programa,mostre: a média de idade do grupo, qual
é o nome do mais velho e quantas mulheres tem menos de 20 anos.'''
from time import sleep
print('\033[0;33m')
print('='*25)
print('   ANALISADOR COMPLETO')
print('='*25)
print('\033[m')
sleep(0.5)
soma = 0
cont = 0
media = 0
maior = 0
m21 = 0
maisvelho = 0
for c in range(1, 5):
    print('------{}ª PESSOA ------'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M]/[F]: ')).strip().upper()
    soma += idade
    cont += 1
    media = soma / cont
    if sexo == 'M':
        if c == 1:
            maior = idade
        else:
            if idade > maior:
                maior = idade
                maisvelho = nome
    elif sexo == 'F':
        if idade < 21:
            m21 += 1
print('A média de idade é {} anos,\n'
      'O nome do homem mais velho é {}\n'
      'Ao todo são {} mulheres com menos de 21 anos'.format(media, maisvelho, m21))

