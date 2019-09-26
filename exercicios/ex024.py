# Faça um programa que leia o nome de uma cidade e verifique se o primeiro nome é a palavra 'SANTO'

cidade = str(input('Em que cidade você mora? ')).strip()
print(cidade[0:5].upper() == 'SANTO')
