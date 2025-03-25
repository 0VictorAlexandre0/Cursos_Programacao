import math
angulo = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo)) #transformar o valor digitado para radiano(trigonometria)
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))

