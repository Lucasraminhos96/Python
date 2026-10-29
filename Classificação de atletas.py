from datetime import date 
atual = date.today().year
ano = int(input('Ano de nascimento :'))
idade = atual - ano 
if idade <= 9 :
     print('''Atleta tem {} anos.
     Classificação : Mirim '''.format(idade))
elif 10 < idade <= 14 :
     print('''Atleta tem {} anos.
     Classificação : INFANTIL '''.format(idade))
elif 15 > idade <= 19 :
     print('''Atleta tem {} anos.
     Classificação : JÚNIOR '''.format(idade))
elif 20 > idade <= 25 :
     print('''Atleta tem {} anos.
     Classificação : SÉNIOR '''.format(idade)) 
elif idade >=26 :
     print('''Atleta tem {} anos.
     Classificação : MASTER '''.format(idade))  