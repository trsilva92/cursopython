# Faça um programa que leia o nome de quatro alunos e imprima na tela os quatro nomes aleatoriamente

from random import shuffle
n1 = str(input('Nome1: '))
n2 = str(input('Nome2: '))
n3 = str(input('Nome3: '))
n4 = str(input('Nome4: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação do trabalho é {}'.format(lista))
