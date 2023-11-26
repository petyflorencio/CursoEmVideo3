#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas.

trip = float(input('How many km is your trip?\n'))
if trip <= 200:
    print('Ok, the ticket for this trip will be R$ {:.2f}.'.format(trip*0.50))
else:
    print('Ok, the ticket for this trip will be R$ {:.2f}.'.format(trip*0.45))
