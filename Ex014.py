# Mostrar temperatura em Cº e em Fº
# Referência: (100°C × 9/5) + 32 = 212°F

cel = float(input('Quantos graus Cº está fazendo na sua região?\n'))
far = (cel * 9/5) + 32
print('Legal, {} Cº corresponde a {} Fº :D'.format(cel, far))
