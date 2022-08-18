'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
 (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

from time import sleep
mensagem = 'Lista ordenada'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

lista = []
for c in range (0,5):
    numeros = int(input(f'Digite o {c+1}º numero: ').strip())
    if c == 0 or numeros > lista[-1]:
        lista.append(numeros)
        print('Adicionado no final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if numeros <= lista[posicao]:
                lista.insert(posicao,numeros)
                print(f'Adicionado na posição {posicao}')
                break
        posicao += 1
print()
print(lista)