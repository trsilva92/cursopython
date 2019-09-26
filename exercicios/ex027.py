# Faça um programa que leia o nome completo de uma pessoa e identifique o seu primeiro e último nome

n = str(input('Digite o nome: ')).strip().upper()
nome = n.split()
print('o nome tem {}'.format(nome))
print('O seu primeiro é {} '.format(nome[0]))
print('O seu último nome é {}'.format(nome[len(nome)-1]))
