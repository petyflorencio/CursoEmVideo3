#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('First segment (in cm):\n'))
r2 = float(input('Second segment (in cm):\n'))
r3 = float(input('Third segment (in cm):\n'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('The segments provided CAN make a triangle!!')
else:
    print('The segments provided CANNOT make a triangle...')