# Faça um programa que leia um número real e imprima na tela a sua porção inteira

from math import trunc
n1 = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n1, int(n1)))
# OU
print('O valor digitado foi {} e sua porção inteira é {}'.format(n1, trunc(n1)))

