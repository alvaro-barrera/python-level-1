import random


def number_select(number_limit):
    return int(input('Ingrese un número del 1 al ' + str(number_limit) + ': '))


def number_low():
    return int(input('Ingrese un número más grande: '))


def number_high():
    return int(input('Ingrese un número más pequeño: '))


def run():
    # VALOR LÍMITE
    number_limit = int(input('Ingrese un número límite: '))
    # LÍMITE MAYOR QUE 1
    while number_limit <= 1:
        number_limit = int(input('Ingrese un número límite válido (> 1): '))
    # VALOR ALEATORIO POR ADIVINAR
    number_random = random.randint(1, number_limit)
    # VALOR INGRESADO POR TECLADO
    number_input = number_select(number_limit)
    # MIENTRAS EL NÚMERO INGRESADO NO SEA IGUAL AL NÚMERO RANDOM
    while number_random != number_input:
        if number_input > number_random:
            number_input = number_high()
        else:
            number_input = number_low()
    # NÚMERO INGRESADO IGUAL A NÚMERO RANDOM
    print('¡Ganaste!')


if __name__ == '__main__':
    run()
