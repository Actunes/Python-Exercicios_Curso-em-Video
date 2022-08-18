'''Faça um programa que leia o comprimento do cateto
oposto e do cateto adjacente de um triangulo ratangulo
calule e mostre o comprimento da hipotenusa'''
print('')
print('='*25)
from math import hypot
Cateto_Oposto = float(input('Cateto Oposto: '))
Cateto_Adjacente = float(input('Cateto Adjacente: '))
Comprimento_Hipotenusa = hypot(Cateto_Adjacente, Cateto_Adjacente)
print('Comprimento da hipotenusa: {:.2f}'.format(Comprimento_Hipotenusa))
print('')

