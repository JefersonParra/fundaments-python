def is_palindrome(word):
    inverted_word = word[::-1]

    if word == inverted_word:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


def run():
    word = input('Escribe una palabra: ')
    word = word.replace(' ', '').lower()

    if len(word) == 0:
        print('¡Escribe una palabra!')
    else:
        is_palindrome(word)


if __name__ == '__main__':
    run()