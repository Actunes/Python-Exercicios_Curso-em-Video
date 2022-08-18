'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores 
e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar 
valores.'''
print('\033[0;33m')
print('='*25)
print('      MAIOR E MENOR')
print('='*25)
print('\033[m')
print('')
numero = 0 
resposta = 'S'
repetido = 0
média = 0
número_total = 0
maior = 0
menor = 0
while resposta in 'S':
    numero = int(input('Digite o valor: '))
    resposta = str(input('Deseja continuar? [S/N] ').strip().upper())
    repetido += 1
    número_total = número_total + numero
    média = número_total / repetido
    if repetido == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print('')
print('Média: {}\nMaior: {}\nMenor: {}'.format(média,maior,menor))
print('')