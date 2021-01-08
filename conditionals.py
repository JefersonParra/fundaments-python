age = int(input('¿Cual es tu edad?:'))

if age >= 18 and age < 60:
    print('Eres mayor de edad')
elif age >= 60:
    print('Eres mayor de edad, pero muy viejo')
else:
    print('Eres menor de edad')