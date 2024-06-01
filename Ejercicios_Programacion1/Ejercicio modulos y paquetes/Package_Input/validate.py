def validate_number(numero: int, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    while numero < minimo or numero > maximo:
        reintentos -= 1
        if reintentos <= 0:
            return None
        print(f"Te quedan {reintentos} reintentos")
        numero = int(input(mensaje_error))
    
    return numero


def validate_sting(longitud: int, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    
    while longitud < minimo or longitud > maximo:
        reintentos -= 1
        if reintentos <= 0:
            return None
        print(f"Te quedan {reintentos} reintentos")

        cadena = input(mensaje_error)
        longitud = len(cadena)


        
    return longitud




