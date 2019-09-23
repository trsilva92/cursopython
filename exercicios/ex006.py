# Imprima no console o dobro, tripo, raiz quadrada, potencia ao quadrado e ao cubo de um numero
num = int(input('Digite um número: '))
print('O dobro do número {} é {}'.format(num, num*2))
print('O tripo do número {} é {}'.format(num, num*3))
print('A raiz quadrada do número {} é {}'.format(num, num**(1/2)))


# Imprima no console a multiplicacao, divisao, divisao inteira, resto da divisao, adicao e subtracao entre dois números
n1 = int(input('Digite o n1: '))
n2 = int(input('Digite o n2: '))
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
a = n1 + n2
s = n1 - n2
print('A multiplicação de {} por {} é {}'.format(n1, n2, m))
print('A divisão de {} por {} é {:.2f}'.format(n1, n2, d))
print('A divisão inteira de {} por {} é {}'.format(n1, n2, di))
print('O resto da divisão entre {} e {} é {}'.format(n1, n2, r))
print('A soma de {} e {} é {}'.format(n1, n2, a))
print('A subtração de {} por {} é {}'.format(n1, n2, s))

# Potencia ao quadrado e ao cubo
print('A potência ao quadrado de {} é {}'.format(n1, n1**2))
print('A potência ao cubo de {} é {}'.format(n1, n1**3))
