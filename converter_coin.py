# OPERACIÓN DE CONVERSIÓN
def operation_converter(coin_income=0, base_coin=3.75):
    if coin_income > 0:
        result = coin_income / base_coin
        result = round(result, 2)
        result = str(result)
    else:
        result = '0'
    return result


def operation_writing():
    # INGRESO POR TECLADO
    coin_income = float(input('¿Cuántos coin_income (PEN) tienes? :'))
    base_coin = 3.75

    if coin_income > 0:
        dollars = coin_income / base_coin
        dollars = round(dollars, 2)
        dollars = str(dollars)
    else:
        dollars = '0'

    opetarion_result = operation_converter(coin_income, base_coin)
    print('Tienes $ ' + opetarion_result + ' USD')


# MENÚ DE CONVERSIÓN
menu = """
Bienvenido al conversor de monedas ☺
1 - Soles PEN
2 - Euros
3 - Salir

Elige una opción: """
base_coin = 0
opcion = int(input(menu))
if opcion == 1:
    base_coin = 3.75
    operation_writing()
elif opcion == 2:
    base_coin = 4.39
    operation_writing()
elif opcion == 3:
    print('Ejecución terminada')
else:
    print('Ninguna acción reconocida')
    print('*'*25)
