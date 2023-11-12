# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado

dias = int(input('Por quantos dias você utilizou o carro alugado?\n'))
km = float(input('Quantos Km você percorreu durante o período de utilização?\n'))
final = (dias * 60) + (km * 0.15)
print('Entendi, então o preço final a se pagar é R$ {}'.format(final))