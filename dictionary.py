def run():
    my_dictionary = {
        'name': 'Jeferson',
        'last_name': 'Parra',
        'age': 19
    }

    # print(my_dictionary['name'])

    # for data in my_dictionary.values():
    #     print(data)

    for key, value in my_dictionary.items():
        print(f'{key} = {value}')

if __name__ == '__main__':
    run()