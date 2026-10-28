num =int(input('Primeiro número :'))
seg = int(input('Segundo número :'))

if num == seg :
    print('O primeiro  numero {} é igual ao segundo número {}. '.format(num,seg))
elif num > seg :
    print('O primeiro número {} é maior que o número {}'.format(num,seg))
elif num < seg :
    print('O primeiro número {} é menor que o número {}.'.format(num,seg))
else:
    print('Tente novamente não entendemos sua resposta.')
     