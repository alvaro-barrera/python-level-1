import random


def generate_password():
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    characters = upper + lower + number
    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)

    password = "".join(password)
    return password


def run():
    password = generate_password()
    print('¡Contraseña generada!')
    print(str(password))


if __name__ == '__main__':
    run()
