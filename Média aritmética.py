m = float(input('insira uma distância em metros:'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A média de {:.1f} metros  corresponde  á  {:.1f} km , {:.1f} hm , {:.1f} dam'.format(m,km,hm,dam))
print('A média de {} metros corresponde á {} dm , {:.1f} cm , {:.1f} mn'.format(m,dm,cm,mm))