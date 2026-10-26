num = int(input('Insira um numnéro :'))
print('''Escolha umas das bases para conversão
[1] Conversão para BINARIO
[2] Conversão para OCTAL
[3]Conversão para HEXADECIMAL'''
    )
Opção = int(input('Insira sua opção :')) 
if Opção == 1:
    print('{} convertido em Binario é {}'.format(num,bin(num)[2:]))
elif Opção == 2 :
    print('{} convertido em Octal é {}'.format(num,oct(num)[2:]))
elif Opção == 3 :
  print('{} convertido em Hexadecimal {}'.format(num,hex(num)[2:]))
else:
   print('Essa opção é incorreta, tente novamente !')