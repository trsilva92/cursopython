# Leia o valor de um produto e imprima no console o valor dele com 5% e 10% de desconto

prod = int(input('O valor do produto é: R$'))
desc1 = prod - (prod*5/100)
desc2 = prod - (prod*10/100)
print('Com um desconto de 5%, o produto sai por R${}'.format(desc1))
print('Com um desconto de 10%, o produto sai por R${}'.format(desc2))


