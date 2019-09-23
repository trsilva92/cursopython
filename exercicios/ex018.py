# Faça um programa que leia o valor de um ângulo e cálcule o seno, cosseno e tangente

from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))
