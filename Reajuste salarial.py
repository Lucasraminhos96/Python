S = float(input('Qual é o salario do funcionário ?'))
r = S * 15 /100
t = r + S
print('Um funcionário que ganha R$ {}, com um aumento de 15 % , passa a receber R$ {:.2f}'.format(S,t))

