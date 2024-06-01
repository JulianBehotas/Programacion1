def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    numero = int(input(mensaje))
    reintentos = reintentos
    while numero < minimo or numero > maximo:
        reintentos -= 1
        print(f"Te quedan {reintentos} reintentos")
        numero = int(input(mensaje_error))
        
        if reintentos == 1:
            return None
        
    return numero

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float | None:
    numero = float(input(mensaje))
    reintentos = reintentos
    while numero < minimo or numero > maximo:
        reintentos -= 1
        print(f"Te quedan {reintentos} reintentos")
        numero = float(input(mensaje_error))
        
        if reintentos == 1:
            return None
        
    return numero





def get_string(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    cadena = input(mensaje)
    longitud = len(cadena)
    reintentos = reintentos
    while longitud < minimo or longitud > maximo:
        reintentos -= 1
        print(f"Te quedan {reintentos} reintentos")
        cadena = input(mensaje_error)
        longitud = len(cadena)
        if reintentos == 1:
            return None
    return longitud
usar = get_string("cadena: ", "Error. Otro cadena: ", 1,10,3)
print(usar)