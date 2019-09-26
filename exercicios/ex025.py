# Faça um programa que leia um nome completo e verifique se possui a palavra 'SILVA'

nome = str(input('Qual o seu nome completo? ')).strip()
print('O nome {} contém a palavra silva? {} '.format(nome.upper(), 'ribeiro' in nome))
