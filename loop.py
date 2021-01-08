def run():
    LIMIT = 1000000
    count = 0
    potency = 2 ** count

    while potency < LIMIT:
        print(f'2 elevado a {count} es igual a: {potency}')
        count = count + 1
        potency = 2 ** count


if __name__ == '__main__':
    run()