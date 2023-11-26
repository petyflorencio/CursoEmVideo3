#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1250,00 calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('How much is your current salary in R$?\n'))
if salary >= 1250:
    print('Alright. You salary will be increased in R$ {}'.format(float(salary*10)/100))
else:
    print('Alright. You alary will be increased in R$ {}'.format(float(salary*15)/100))
