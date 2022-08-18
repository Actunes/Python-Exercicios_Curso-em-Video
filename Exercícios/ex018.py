'''Faca um programa que leia um angulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse angulo'''
print('')
print('='*25)
from math import sin,cos,tan,radians
Angulo = float(input('Digite o Angulo: '))
print('Angulo: {:.2f}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(Angulo,sin(radians(Angulo)),cos(radians(Angulo)),tan(radians(Angulo))))
print('')
