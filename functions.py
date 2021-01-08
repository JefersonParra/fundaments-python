# def printer_message():
#     print('Mensaje especial')
#     print('¡Estoy aprendiendo a usar funciones!')

# printer_message()
# printer_message()
# printer_message()

def printer_message(option):
    print('Hola')
    print('Cómo estás')
    print('Elejiste la opción ' + option)
    print('Adiós')

option = input('Elije una opción (1, 2, 3): ')

if option == '1':
    printer_message(option)
elif option == '2':
    printer_message(option)
elif option == '3':
    printer_message(option)
else:
    print('Elije una opción correcta')