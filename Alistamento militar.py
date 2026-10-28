ali = int(input('Digite em qual ano voçê nasceu :'))
n1 = 2026-ali
n2 = n1-18
if n1 > 18 :
    print('''Voçê nasceu em {} e está com {} anos ja passou {} anos do seu alistamento.'''.format(ali,n1,n2)) 
elif n1 == 18 :
    print('Voçê nasceu em {} e  tem {} anos e deve se alistar IMEDIATAMENTE !'.format(ali,n1))
else:
    print('Voçê nasceu em {} voçê tem {} anos e faltam {} anos para o seu alistamento.'.format(ali,n1,n2))