frase = str(input('Escreva uma frase :')).upper().strip()
print('A letra A aparece {} na sua frase .'.format(frase.count('A')))
print('A primeira letra A aparece na {} posição.'.format(frase.find('A')+1.))
print('A ultima letra A aparece na {} posição.'.format(frase.rfind('A')+1))