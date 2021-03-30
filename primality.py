def is_primality(number):
    if number == 1:
        return False
    else:
        count = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False


def run():
    number = int(input('Ingrese un número: '))
    if is_primality(number):
        res = 'Es primo'
    else:
        res = 'No es primo'
    print(res)


if __name__ == '__main__':
    run()
