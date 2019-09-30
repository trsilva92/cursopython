# Faça um programa que leia um nome completo e verifique se possui a palavra 'SILVA'

nome = str(input('Qual o seu nome completo? ')).strip()
print('O nome {} contém a palavra ribeiro? {} '.format(nome.upper(), 'ribeiro' in nome))
