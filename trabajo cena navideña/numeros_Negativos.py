def analizar_numeros():
    numeros = []
    numero = int(input("Ingrese un número positivo (ingrese un negativo para terminar): "))
    
    while numero >= 0:
        numeros.append(numero)
        numero = int(input("Ingrese otro número positivo (ingrese un negativo para terminar): "))

    
    total_numeros = len(numeros)
    
    
    numeros_pares = [num for num in numeros if num % 2 == 0]
    total_pares = len(numeros_pares)

    
    promedio_pares = sum(numeros_pares) / total_pares if total_pares > 0 else 0

    
    numeros_impares = [num for num in numeros if num % 2 != 0]
    promedio_impares = sum(numeros_impares) / (total_numeros - total_pares) if total_numeros > total_pares else 0

    
    menores_10 = len([num for num in numeros if num < 10])

    
    entre_20_y_50 = len([num for num in numeros if 20 <= num <= 50])

    
    mayores_100 = len([num for num in numeros if num > 100])

    
    print(f"Total de números ingresados: {total_numeros}")
    print(f"Total de números pares ingresados: {total_pares}")
    print(f"Promedio de los números pares: {promedio_pares}")
    print(f"Promedio de los números impares: {promedio_impares}")
    print(f"Cuantos números son menores que 10: {menores_10}")
    print(f"Cuantos números están entre 20 y 50: {entre_20_y_50}")
    print(f"Cuantos números son mayores que 100: {mayores_100}")

analizar_numeros()