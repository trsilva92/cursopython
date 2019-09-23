# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 O nome com todas as letras maíusculas e depois minúsculas
# 2 Quantas letras tem no total (sem considerar espaços)
# 3 Quantas letras tem o primeiro e o último nome

nome = str(input('Digite o nome completo: '))
print('Seu nome em maíusculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))

print('O primeiro nome possui {} letras'.format(nome.find(' ')))
# OU
separa = nome.split()
print('O primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0])))



