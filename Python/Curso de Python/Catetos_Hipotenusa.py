#Faça um programa que leia o comprimento do cateto oporto e do
#cateto adjascente de um triângulo retângulo, calcule e mostre o
#comprimento da hipotenusa.

#Feito de maneira matemática sem importação
Cateto_Oposto = float(input('Comprimento do cateto oposto: '))
Cateto_Adjascente = float(input('Comprimento do cateto adjascente: '))
Hipotenusa = (Cateto_Oposto ** 2 + Cateto_Adjascente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(Hipotenusa))

#Feito com Math

from math import hypot
Cateto_Oposto = float(input('Comprimento do cateto oposto: '))
Cateto_Adjascente = float(input('Comprimento do cateto adjascente: '))
Hipotenusa = hypot(Cateto_Oposto, Cateto_Adjascente)
print('A hipotenusa vai medir {:.2f}'.format(Hipotenusa))
