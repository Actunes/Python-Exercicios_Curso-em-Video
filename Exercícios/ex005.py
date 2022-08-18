#Faça um programa que leia um número inteiro e mostre na tela o seu 
#sucessor e seu antecessor.

Número = int(input('Digite um número: '))
Sucessor = Número + 1
Antecessor = Número - 1
print('Número: {} \nSucessor: {} \nAntecessor:{}'.format(Número ,Sucessor, Antecessor))