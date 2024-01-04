Eplicacion del desarrollo o solucion del primer punto (sumar tres numeros)

def sumar_numeros():
    while True:
				"""variables: internas: n1, n2, n3, almacenan los numeros ingresados por el usuario
				   suma: almacena el resultado de la suma de n1, n2, n3 """
							# se pide al usuario que ingrese tres numeros 
        try:
            n1 = int(input("Por favor, ingrese el primer número que desea sumar: "))
            n2 = int(input("Por favor, ingrese el segundo número que desea sumar: "))
            n3 = int(input("por favor, ingrese el tercer numero que desea sumar: "))
												#se calcula la sumatoria de los tres numeros 
            suma = n1 + n2 + n3 
												# se imprime el resultado de los tres numeros enteros tras ser sumados
            print("El resultado de la suma de los tres números es:", suma)
            return suma
        except ValueError:
            print("El valor que ingresó no es un número. Por favor, ingrese un número e intente de nuevo.")
												
while True:
    resultado = sumar_numeros()
    opcion = input("¿Desea sumar otros números? (Sí/No): ").lower()
				# condicion de salida: " si el usuario escribe algo diferente a "si" el bucle rompe y el programa termina
    if opcion != 'si':
        break


2): explicacion del desarrolo o solucion del segundo y tercer punto con comentarios(IMC indice de masa corporal en los estudiantes)

# Función para calcular el IMC y determinar la categoría
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def determinar_categoria(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad grado I"
    elif 35 <= imc < 39.9:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"

# Variables para contadores
peso_ideal_count = 0
obesidad_i_count = 0
obesidad_ii_count = 0
obesidad_iii_count = 0
sobrepeso_count = 0

# Registro de estudiantes
for _ in range(20):
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad del estudiante: "))
    peso = float(input("Peso del estudiante (en kg): "))
    altura = float(input("Altura del estudiante (en metros): "))

    # Calcular el IMC y determinar la categoría
    imc = calcular_imc(peso, altura)
    categoria = determinar_categoria(imc)

    # Mostrar detalles del estudiante y categoría
    print(f"\nNombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"IMC: {imc:.2f}")
    print(f"Categoría: {categoria}\n")

    # Contar estudiantes en cada categoría
    if categoria == "Peso normal":
        peso_ideal_count += 1
    elif categoria == "Obesidad grado I":
        obesidad_i_count += 1
    elif categoria == "Obesidad grado II":
        obesidad_ii_count += 1
    elif categoria == "Obesidad grado III":
        obesidad_iii_count += 1
    elif categoria == "Sobrepeso":
        sobrepeso_count += 1

# Mostrar el reporte final
print("\nReporte Final:")
print(f"a. Peso ideal: {peso_ideal_count} estudiantes")
print(f"b. Obesidad grado I: {obesidad_i_count} estudiantes")
print(f"c. Obesidad grado II: {obesidad_ii_count} estudiantes")
print(f"d. Obesidad grado III: {obesidad_iii_count} estudiantes")
print(f"e. Sobrepeso: {sobrepeso_count} estudiantes")

3): explicacion del desarrolo o solucion del cuarto punto con comentarios(ingresar numeros enteros positivos y mostrar el total de numeros pares, inpares, etc.)

def analizar_numeros():
   # numeros: Una lista vacía para almacenar los números ingresados por el usuario.
    numeros = []
    numero = int(input("Ingrese un número positivo (ingrese un negativo para terminar): "))
				
    # La función inicia con un ciclo while que pide al usuario ingresar números. Este ciclo continúa hasta que el usuario ingresa un número negativo.
				
    while numero >= 0:
        numeros.append(numero)
        numero = int(input("Ingrese otro número positivo (ingrese un negativo para terminar): "))

    # total_numeros: Calcula el número total de entradas almacenadas en la lista
				
    total_numeros = len(numeros)
    
    # numeros_pares: Utiliza comprensión de listas para crear una nueva lista con solo los números pares de numeros.
				
    numeros_pares = [num for num in numeros if num % 2 == 0]
				
				# total_pares: Calcula el número de elementos en numeros_pares.
				
    total_pares = len(numeros_pares)

    # promedio_pares: Calcula el promedio de los números pares. Si no hay números pares, el promedio es 0.
				
    promedio_pares = sum(numeros_pares) / total_pares if total_pares > 0 else 0

    # numeros_impares: Similar a numeros_pares, pero para números impares.
				
    numeros_impares = [num for num in numeros if num % 2 != 0]

				# promedio_impares: Calcula el promedio de los números impares. Si no hay números impares, el promedio es 0.
				
    promedio_impares = sum(numeros_impares) / (total_numeros - total_pares) if total_numeros > total_pares else 0

    # menores_10: Cuenta cuántos números en numeros son menores que 10.
				
    menores_10 = len([num for num in numeros if num < 10])

    # entre_20_y_50: Cuenta cuántos números están en el rango de 20 a 50, inclusive.
				
    entre_20_y_50 = len([num for num in numeros if 20 <= num <= 50])

    #mayores_100: Cuenta cuántos números son mayores que 100.
				
    mayores_100 = len([num for num in numeros if num > 100])

    # El programa imprime todos los resultados analizados: totales, promedios, y conteos según los criterios especificados.
				
    print(f"Total de números ingresados: {total_numeros}")
    print(f"Total de números pares ingresados: {total_pares}")
    print(f"Promedio de los números pares: {promedio_pares}")
    print(f"Promedio de los números impares: {promedio_impares}")
    print(f"Cuantos números son menores que 10: {menores_10}")
    print(f"Cuantos números están entre 20 y 50: {entre_20_y_50}")
    print(f"Cuantos números son mayores que 100: {mayores_100}")

analizar_numeros()

4): explicacion del desarrolo o solucion del cuarto punto con comentarios(registro de sismos en multiples ciudades)

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

# lista de multiples opciones del programa para registrar nombre de ciudad, cantidad de sismos, etc. 
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
