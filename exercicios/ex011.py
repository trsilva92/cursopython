# Digite a altura e largura de uma parede e cálcule a sua área;
# Cálcula a quantidade de tinta necessária para pintar parede, sendo que 1L de tinta pinta 2m²;

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
print('Sabendo que a largura é {} e a altura é {}, então a área da parede é {}m²'.format(largura, altura, area))
qtdtinta = area / 2
print('Sendo assim, a quantidade necessária de tinta é de {}L'.format(qtdtinta))

