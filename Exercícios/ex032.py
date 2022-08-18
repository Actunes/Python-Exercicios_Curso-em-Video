'''Faça um programa que leia um ano qualquer 
e nistre se eke pe BISSEXTO'''
print('')
print('='*25)
print('')
Ano = int(input('Digit o ANO: '))
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print('O ano digitado é BISSEXTO!')
else:
    print('O ano digitado NÃO é BISSEXTO!')    
print('')