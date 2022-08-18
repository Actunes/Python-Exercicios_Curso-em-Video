'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do internacional.'''

from requests_html import HTMLSession
from time import sleep

mensagem = 'TABELA DO BRASILEIRAO'
lido = len(mensagem) + 4
print('=' * lido)
print(' ',mensagem)
print('=' * lido)

escolha_tabela = input(str('Qual tabela você deseja ver? [A-B] ')).lower().strip()
while True:
    while escolha_tabela not in 'ab':
        escolha_tabela = input(str('Qual tabela você deseja ver? [A-B] ')).lower().strip()
    break

if escolha_tabela == 'a':
    session = HTMLSession()
    request = session.get('https://esportes.estadao.com.br/classificacao/futebol/campeonato-brasileiro-serie-a/2022')
    nome = request.html.find('.time-name')
elif escolha_tabela == 'b':
    session = HTMLSession()
    request = session.get('https://esportes.estadao.com.br/classificacao/futebol/campeonato-brasileiro-serie-b/2022')
    nome = request.html.find('.time-name')

tabela = (nome[0].text, nome[1].text, nome[2].text, nome[3].text, nome[4].text,
          nome[5].text, nome[6].text, nome[7].text, nome[8].text, nome[9].text,
          nome[10].text, nome[11].text, nome[12].text, nome[13].text, nome[14].text,
          nome[15].text, nome[16].text, nome[17].text, nome[18].text, nome[19].text)

print()
print(f'Os 5 primeiros times: {tabela[:5]}')
print()
print(f'Os ultimos 4 colocados: {tabela[-4:]}')
print()
print(f'Times em ordem alfabética: {sorted(tabela)}')
print()
if escolha_tabela == 'a':
    print(f'Posição do internacional: {tabela.index("Internacional")+1}ª')
print()