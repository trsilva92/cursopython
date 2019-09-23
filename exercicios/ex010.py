# Leia um valor em reais e calcule a quantidade de dolar possivel de compra

qtdReal = float(input('Quanto dinheiro você tem na carteira? R$'))
qtdDolar = qtdReal / 4.09
qtdEuro = qtdReal / 4.50
print('Com R${:.2f} você pode comprar US${:.2f} e EU${:.2f}'.format(qtdReal, qtdDolar, qtdEuro))
