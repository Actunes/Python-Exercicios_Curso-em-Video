'''Refaça o DESAFIO 035 dos triângulos, acrescentando
o recurso de mostrar que tipo de tirangulo será mostrado

- Equilátero: todos os lados iguais
- Isósceles: dois lagos iguais
- Escaleno: Todos os lados diferentes'''

from time import sleep
print('\033[0;35m')
print('='*25)
print('    tipo de triangulo')
print('='*25)
print('\033[m')
sleep(0.5)

Primeira_Reta = int(input('Digite o comprimento da primeira reta: '))
Segunda_Reta = int(input('Digite o comprimento da segunda reta: '))
Terceira_Reta = int(input('Digite o comprimento da terceira reta: '))

if Primeira_Reta > Segunda_Reta + Terceira_Reta and Segunda_Reta < Primeira_Reta + Terceira_Reta and Terceira_Reta < Primeira_Reta + Segunda_Reta:
    if Primeira_Reta != Segunda_Reta != Terceira_Reta:
        triangulo = 'Escaleno'
    elif Primeira_Reta == Segunda_Reta == Terceira_Reta:
        triangulo = 'Equilatero'
    else:
        triangulo = 'Isósceles'
    print('As retas acima podem formar um triângulo e aponta um TRIANGULO {}'.format(triangulo))
else:
    print('Os segmentos acima não podem formar triângulos')
print('')