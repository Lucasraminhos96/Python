import random
n1 = str(input('Primeiro aluno :'))
n2 = str(input('Segundo aluno :'))
n3 = str(input('Treceiro aluno :'))
n4 = str(input('Querto aluno :'))
lista = [n1,n2,n3,n4]
esc = random.choice(lista)
print('O aluno escolhido foi: {}'.format(esc))