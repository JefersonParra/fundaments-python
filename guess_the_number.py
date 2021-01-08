import random


def run():
    number_random = random.randint(1, 100)
    number = int(input('Escribe un número del 1 a 100: '))

    while number != number_random:
        if number < number_random:
            print('Escribe un número más grande')
        else:
            print('Escribe un número más pequeño')

        number = int(input('Escribe otro número: '))

    print('¡Ganaste!')


if __name__ == '__main__':
    run()