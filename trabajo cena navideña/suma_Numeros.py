def sumar_numeros():
    while True:
        try:
            n1 = int(input("Por favor, ingrese el primer número que desea sumar: "))
            n2 = int(input("Por favor, ingrese el segundo número que desea sumar: "))
            suma = n1 + n2
            print("El resultado de la suma de los dos números es:", suma)
            return suma
        except ValueError:
            print("El valor que ingresó no es un número. Por favor, ingrese un número e intente de nuevo.")
while True:
    resultado = sumar_numeros()
    opcion = input("¿Desea sumar otros números? (Sí/No): ").lower()
    if opcion != 'si':
        break