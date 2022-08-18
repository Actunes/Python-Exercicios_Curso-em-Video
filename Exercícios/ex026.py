'''Faça um programa que leia uma frase pelo teclado
e mostre: 
Quantas vezes aparece a letra 'a'.
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.'''

print('')
print('='*25)
Frase = str(input('Digite uma frase: ')).strip().lower()
print('Vezes em que "a" aparece: {}'.format(Frase.count('a')))
print('Primeira posição: {}'.format(Frase.find('a')+1))
print('Ultima posição: {}'.format(Frase.rfind('a')+1))
print('')