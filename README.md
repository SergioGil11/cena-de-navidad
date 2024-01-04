eplicacion del primer punto, desarrollo o la solucion del programa(sumar tres numeros enteros)

 Función sumar_numeros()
- *Propósito*: Sumar tres números ingresados por el usuario.
- *Variables Internas*:
  - n1, n2, n3: Almacenan los números ingresados por el usuario. Son de tipo int.
  - suma: Almacena el resultado de la suma de n1, n2 y n3.
- *Flujo de la función*:
  1. *Bucle while True*: Este bucle hace que la función siga pidiendo números hasta que se ingresen correctamente.
  2. *Bloque try-except*: Se utiliza para manejar excepciones. En este caso, atrapa errores de valor (como ingresar letras en lugar de números).
  3. *Input y Conversión a int*: Los números se leen como cadenas (string) desde el teclado y luego se convierten a enteros (int).
  4. *Cálculo de la Suma y Salida*: Calcula la suma de los tres números y la imprime. Luego, retorna el valor de la suma.
  5. *Manejo de Excepciones*: Si se introduce un valor no numérico, se muestra un mensaje de error y se solicita nuevamente la entrada.

### Bucle Principal
- *Variables*:
  - resultado: Almacena el valor retornado por la función sumar_numeros().
  - opcion: Almacena la respuesta del usuario a la pregunta de si desea continuar sumando números.
- *Flujo del Programa Principal*:
  1. *Llamada a sumar_numeros()*: El programa llama a la función sumar_numeros() y almacena el resultado en resultado.
  2. *Input del Usuario*: Pregunta al usuario si desea continuar sumando números.
  3. *Conversión a Minúsculas*: Convierte la respuesta del usuario a minúsculas para facilitar la comparación.
  4. *Condición de Salida*: Si el usuario escribe algo diferente de "si", el bucle se rompe y el programa termina.

### Flujo General del Programa
El programa se ejecuta en un bucle continuo, pidiendo al usuario que ingrese tres números para sumarlos. Tras mostrar el resultado de la suma, pregunta si desea continuar. Si el usuario responde algo diferente a "si", el programa termina.
