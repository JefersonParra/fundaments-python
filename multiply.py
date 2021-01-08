def multiply(x, y):
    for i in range(0, x + 1):
        print('{0}'.format('=' * 15))

        for j in range(0, y + 1):
            result = i * j
            print('{0:^3} x {1:^3} = {2:^3}'.format(i, j, result))

        print('{0}'.format('=' * 15))

if __name__ == '__main__':
    x = int(input("Hasta que tabla de multiplicar quiere: "))
    y = int(input("Hasta que valor: "))
    multiply(x, y)