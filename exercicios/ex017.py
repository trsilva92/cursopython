# Faça um programa que leia o comprimento do cateto oposto, cateto adjacente de um triângulo retângulo
# Cálcule o comprimento da hipotenusa

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hipo = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
