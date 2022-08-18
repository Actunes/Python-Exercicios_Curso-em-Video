'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão 
passada está com os parênteses abertos e fechados na ordem correta.'''

from time import sleep
mensagem = 'Validando expressões matemáticas'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)
print()
sleep(1)

expressao = str(input('Digite a expressão: ')).strip
lista = []
for parenteses in expressao:
    if parenteses == '(':
        lista.append('(')
    elif parenteses == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão valida.')
else:
    print('Expressão invalida.')
    

