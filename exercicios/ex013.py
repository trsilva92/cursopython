# Leia o salario de um funcionario, e imprima no console o valor com 15% de aumento

sal = float(input('Digite o salário do funcionário: R$'))
aumento = sal + (sal * 15 / 100)
print('O salario do funcionário de R${:.2f} com 15% de aumento, agora é de R${:.2f}'.format(sal, aumento))
