def run():
    # print('Números primos del 1 - 100')

    # for i in range(1, 100):
    #     for j in range(1, 100):
    #         if i == j:
    #             print(i)
    #             break
    #         elif j == 1:
    #             continue
    #         elif i % j == 0:
    #             break

    # check if is prime number
    number = int(input('Escribe un número: '))

    for i in range(1, number + 1):
        if number == i:
            print('Es número primo')
            break
        elif i == 1:
            continue

        if number % i != 0:
            continue
        else:
            print('No es número primo')
            break


if __name__ == '__main__':
    run()