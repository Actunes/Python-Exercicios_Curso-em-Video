#Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo
#e raiz quadrada.

Número = float(input('Digite um número: '))
print('Número: {} \nDobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}'.format(Número, Número * 2 ,Número * 3 ,Número ** (1/2)))
