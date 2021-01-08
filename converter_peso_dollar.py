pesos = float(input('¿Cuántos pesos colombianos tienes?: '))

value_dollar = 3433

dollars = str(round(pesos / value_dollar, 2))

print('Tienes $' + dollars + ' dólares')