'''Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem
ou não formar um tiângulo.'''

print('')
print('='*25)
print('') 
Primeira_Reta = int(input('Digite o comprimento da primeira reta: '))
Segunda_Reta = int(input('Digite o comprimento da segunda reta: '))
Terceira_Reta = int(input('Digite o comprimento da terceira reta: '))
if Primeira_Reta > Segunda_Reta + Terceira_Reta and Segunda_Reta < Primeira_Reta + Terceira_Reta and Terceira_Reta < Primeira_Reta + Segunda_Reta:
    print('As retas acima podem formar um triângulo','vermelho')
else:
    print('Os segmentos acima não podem formar triângulos','vermelho')
    print('')