def run(iterator):
    potency = 2 ** iterator

    if potency >= 1000:
        print('Fin')
    else:
        print(f'2 ** {iterator} = {potency}')
        iterator = iterator + 1
        run(iterator)


if __name__ == '__main__':
    run(0)