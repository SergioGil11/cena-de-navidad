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