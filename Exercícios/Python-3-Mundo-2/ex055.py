'''Faça um programa que leia o peso de cinco pessoas. No final,mostre qual foi o maior e o menor peso lido'''
from time import sleep
print('\033[0;33m')
print('='*25)
print('      MENOR E MAIOR')
print('='*25)
print('\033[m')
sleep(0.5)
maior = 0
menor = 0
for c in range (1,6):
    peso_pessoa = float(input('Peso da {}ª pessoa: '.format(c)))
    if peso_pessoa == 1:
        maior = peso_pessoa
        menor = peso_pessoa
    else:
        if peso_pessoa > maior:
            maior = peso_pessoa
        if peso_pessoa < menor:
            menor = peso_pessoa
print('')
print('Maior: {}\nMenor: {}'.format(maior,menor))