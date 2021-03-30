# OPERACIÓN DE CONVERSIÓN
def operation_converter(coin_income=0, base_coin=3.75):
    if coin_income > 0:
        result = coin_income / base_coin
        result = round(result, 2)
        result = str(result)
    else:
        result = '0'
    return result

def operation_writing(base_coin, coin_title):
    # INGRESO POR TECLADO
    coin_income = float(input('¿Cuántos ' + coin_title + ' tienes? :'))
    opetarion_result = operation_converter(coin_income, base_coin)
    print('Tienes $ ' + opetarion_result + ' (USD)')

# MENÚ DE CONVERSIÓN
menu = """
Bienvenido al conversor de monedas ☺
1 - Soles PEN
2 - Euros
3 - Salir

Elige una opción: """

# ENTRADAS A CONVERSIÓN
base_coin = 0
opcion = int(input(menu))
if opcion == 1:
    base_coin = 3.75
    coin_title = 'SOLES (PEN)'
    operation_writing(base_coin, coin_title)
elif opcion == 2:
    base_coin = 4.39
    coin_title = 'EUROS (EUR)'
    operation_writing(base_coin, coin_title)
elif opcion == 3:
    print('Ejecución terminada')
else:
    print('Ninguna acción reconocida')
    print('*' * 25)
