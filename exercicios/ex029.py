# Faça um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h monstre uma mensagem dizendo que ele foi multado
# O valor da multa é de R$7,00 para cada km acima do limite

velocidade = int(input('Digite a velocidade: '))
print('A velocidade registrada foi de {}km/h'.format(velocidade))

if velocidade > 80:
    #velocidade = velocidade * 7
    print('Você foi multado')
    print('E o valor da multa é de R${}'.format(velocidade))
else:
    print('Velocidade dentro do permitido')
