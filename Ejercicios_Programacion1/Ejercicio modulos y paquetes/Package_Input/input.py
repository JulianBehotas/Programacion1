from validate import *


def get_int(mensaje: str) -> int:
    numero = input(mensaje)
    numero = int(numero)
    numero_validado = validate_number(numero, "Error, Ingrese nuevamente un numero: ", 1, 10, 3)

    return numero_validado


def get_float(numero: int, mensaje: str) -> float:
    numero = input(mensaje)
    numero = float(numero)

    return numero



def get_string(mensaje: str) -> int:
    cadena = input(mensaje)
    longitud = len(cadena)
    validar_cadena = validate_sting(longitud, "Error. Ingrese nuevamente una cadena: ",1,10,3)

    return validar_cadena


usar = get_string("Ingrese una cadena: ")
print(usar)
