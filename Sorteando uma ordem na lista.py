import random
n1 = str(input('primeira nome :'))
n2 =str (input('Segundo nome :'))
n3 = str(input('Terceiro nome :'))
n4 = str(input('Quarto nome :'))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem foi {}'.format(lista))
