# Leia a quantidade de km percorridos por um carro alugado e a quantidade de dias que ele foi alugado;
# Calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado;

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
custoDia = dias * 60
custoKm = km * 0.15
print('O valor a ser pago pelo aluguel é de R${:.2f} e pelos km rodados é de R${:.2f}'.format(custoDia, custoKm))


