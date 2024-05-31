empleados_de_encuesta = 0
porcentaje_empleado = 0
edad_maxima = 0
nombre_de_persona = ""
tecnologia_persona = ""

for i in range(10):
    nombre = input("Ingrese nombre: ")

    edad = input("Ingrese edad: ")
    edad = int(edad)
    while edad < 18:
        print("Error. Debe ser mayor a 18")
        edad = input("Ingrese edad: ")
        edad = int(edad)

    genero = input("Ingrese genero. Masculino - Femenino - Otro: ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        print("Error")
        genero = input("Ingrese genero. Masculino - Femenino - Otro: ")

    tecnologia = input("Ingrese tecnologia. IA - RV/RA - IOT: ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        print("Error")
        tecnologia = input("Ingrese tecnologia. IA - RV/RA - IOT: ")

    if genero == "Masculino" and (tecnologia == "IA" or tecnologia =="IOT") and (edad >= 25 and edad <= 50):
        empleados_de_encuesta += 1 #Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.

    if tecnologia != "IA" and (genero != "Femenino" or edad > 33 and edad < 40):
        porcentaje_empleado += 1

    if edad > edad_maxima:
        edad_maxima = edad
        
    if edad == edad_maxima and genero == "Masculino":
        nombre_de_persona = nombre
        tecnologia_persona = tecnologia




porcentaje_total = (porcentaje_empleado / 10) * 100
print(f"Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive: {empleados_de_encuesta}")
print(f"Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40: {porcentaje_total}%")
print(f"Nombre y tecnología que votó, de los empleados deL género masculino con mayor edad. Nombre: {nombre_de_persona} Tecnologia: {tecnologia_persona}")






