# Faça um programa que o computador pense em u número e o usuário tente adivinhar
# Em seguida mostre na tela se você acertou ou errou na escolha do número

from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print('Ops...você errou! Eu pensei no número {}'.format(computador))
