import random


def generate_password():
    # variables
    upper_letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
    lower_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
    symbols = ('!', '#', '$', '%', '&', '/', '(', ')')
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    characters = upper_letters + lower_letters + symbols + numbers
    password = []

    # choice characters and creation of password
    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)

    return ''.join(password)


def run():
    password = generate_password()

    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()