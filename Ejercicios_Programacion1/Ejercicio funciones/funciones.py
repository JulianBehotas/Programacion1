import math
def solicitar_numero():
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    return numero

def solicitar_numero_flotante():
    numero = input("Ingrese un numero: ")
    numero = float(numero)
    return numero

def solicitar_cadena():
    cadena = input("Ingrese una palabra: ")
    return cadena

def calcular_area_circulo(radio:int) -> int:
    perimetro = 2 * math.pi * radio
    return perimetro

def verificar_par_impar(numero):
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

def encontrar_maximo(numero1, numero2, numero3):
    maximo = numero1
    if numero2 > maximo:
        maximo = numero2
    if numero3 > maximo:
        maximo = numero3
    return maximo

def calcular_potencia(base, exponente):
    resultado = base ** exponente
    return resultado












