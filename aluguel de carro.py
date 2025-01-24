dia = int(input('Quantos dia alugado:'))
km = float(input('Quantos km  rodado: '))
m = 60*dia
l = km*0.15
r =m+l
print('total a pagar é de R${:.2f} reais '.format(r))