medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {} metros equivale a: \n{} Quilômetros; \n{} Hectômetros; \n{} Decâmetros;'
      '\n{} Decímetros; \n{} Centímetros; \n{} Milímetros.'.format(medida, km, hm, dam, dm, cm, mm))