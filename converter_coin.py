# variables
pesos = 0
menu = '''
**********************************
CONVERTIDOR DE DÓLARES
**********************************

Selecciona la opción de la moneda:

1) Argentina
2) Colombia
3) México

**********************************
'''

# function
def converter(type_peso, value_peso):
    pesos = str(round(dollars * value_peso))
    print('Tienes $' + pesos + ' pesos ' + type_peso)

# request data
option = input(menu)

dollars = float(input('¿Cuántos dólares tienes?: '))

# conditional
if option == '1':
    converter('argentinos', 85)
elif option == '2':
    converter('colombianos', 3500)
elif option == '3':
    converter('mexicanos', 17)
else:
    print('Elije una opción correcta')