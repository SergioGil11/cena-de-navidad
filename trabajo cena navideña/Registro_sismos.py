def registrar_sismo(ciudades, ciudad_actual, sismos):
    print(f"Registrando sismos para {ciudad_actual}")
    sismos_ciudad = []
    for i in range(len(ciudades[0])):
        magnitud = float(input(f"Ingrese la magnitud del sismo {i + 1}: "))
        sismos_ciudad.append(magnitud)
    sismos.append(sismos_ciudad)

# Módulo para buscar sismos por ciudad
def buscar_sismos(ciudades, ciudad_buscada, sismos):
    if ciudad_buscada in ciudades:
        indice_ciudad = ciudades.index(ciudad_buscada)
        sismos_ciudad = sismos[indice_ciudad]
        print(f"Sismos registrados en {ciudad_buscada}: {sismos_ciudad}")
    else:
        print(f"No se encontraron registros para {ciudad_buscada}")

# Módulo para generar el informe de riesgo
def informe_riesgo(ciudades, sismos):
    for i in range(len(ciudades)):
        promedio = sum(sismos[i]) / len(sismos[i])
        if promedio < 2.5:
            print(f"{ciudades[i]}: Amarillo (Sin riesgo)")
        elif 2.6 <= promedio <= 4.5:
            print(f"{ciudades[i]}: Naranja (Riesgo medio)")
        else:
            print(f"{ciudades[i]}: Rojo (Riesgo alto)")

# Programa principal
ciudades = []
sismos = []

while True:
    print("\nMenu:")
    print("1. Registrar Ciudad")
    print("2. Registrar Sismo")
    print("3. Buscar Sismos por Ciudad")
    print("4. Informe de Riesgo")
    print("5. Salir")

    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        ciudad = input("Ingrese el nombre de la ciudad: ")
        ciudades.append(ciudad)
    elif opcion == 2:
        if not ciudades:
            print("Primero registre al menos una ciudad.")
        else:
            ciudad_actual = input("Ingrese el nombre de la ciudad para registrar sismos: ")
            if ciudad_actual in ciudades:
                registrar_sismo(ciudades, ciudad_actual, sismos)
            else:
                print("La ciudad ingresada no existe.")
    elif opcion == 3:
        if not ciudades:
            print("No hay ciudades registradas.")
        else:
            ciudad_buscada = input("Ingrese el nombre de la ciudad para buscar sismos: ")
            buscar_sismos(ciudades, ciudad_buscada, sismos)
    elif opcion == 4:
        if not ciudades:
            print("No hay ciudades registradas.")
        else:
            informe_riesgo(ciudades, sismos)
    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")