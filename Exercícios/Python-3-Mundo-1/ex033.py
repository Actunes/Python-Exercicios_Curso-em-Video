'''Faça um programa que leia tres números e mostre
qual é o maior e qual é o menor.'''

print('')
print('='*25)
print('')
Número_Usuario_1 = float(input('Digite o primeiro número: '))
Número_Usuario_2 = float(input('Digite o segundo número: '))
Número_Usuario_3 = float(input('Digite o segundo número: '))
if Número_Usuario_1 > Número_Usuario_2 and Número_Usuario_3:
    maior = Número_Usuario_1 
if Número_Usuario_1 < Número_Usuario_2 > Número_Usuario_3:
    maior = Número_Usuario_2
if Número_Usuario_1 and Número_Usuario_2 < Número_Usuario_3:
    maior = Número_Usuario_3
if Número_Usuario_1 < Número_Usuario_2 and Número_Usuario_3:
    menor = Número_Usuario_1
if Número_Usuario_1 > Número_Usuario_2 < Número_Usuario_3:
    menor = Número_Usuario_2
if  Número_Usuario_1 and Número_Usuario_2 > Número_Usuario_3:
    menor = Número_Usuario_3
if Número_Usuario_1 == Número_Usuario_2 == Número_Usuario_3:
    menor = Número_Usuario_1 
    maior = Número_Usuario_3
print('Maior Número: {:.0f}\nMenor Número: {:.0f}'.format(maior,menor))
print('')

