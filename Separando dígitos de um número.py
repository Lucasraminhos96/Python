num =int(input('informe um número: '))
u = num//1%10
d = num//10%10
c = num//100%10
mi = num//1000%10
print('Analisando o número {}'.format(num))
print('Unidade :{}'.format(u))
print('Dezena: {} '.format(d))
print('Centena: {}'.format(c))
print('Milhares : {}'.format(mi))
