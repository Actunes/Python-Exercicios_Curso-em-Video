#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo 
#primitivo e todas as informações possiveis sobre ela.

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é',type(algo))
print('')
print('Só tem espaços?',algo.isspace())
print('')
print('É um número?',algo.isnumeric())
print('')
print('É alfabético?',algo.isalpha())
print('')
print('É alphanumerico?',algo.isalnum())
print('')
print('Está em maiscular?',algo.isupper())
print('')
print('Está em minusculas?',algo.islower())
print('')
print('Está capitalizada?',algo.istitle())