#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

#Erros: não converti para radianos

import math
ang = float(input('Me diga os graus de um ângulo qualquer para que eu possa calcular seu seno, cosseno e tangente: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo que digitou foi de {} º.\n'
      'Seu seno equivale a {:.2f}, seu cosseno {:.2f} e sua tangente {:.2f}.'.format(ang,sen,cos,tan))