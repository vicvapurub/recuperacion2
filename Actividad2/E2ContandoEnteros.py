'''

| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 16/01/2024
| Ejercicio2: Notas Altas y Notas Bajas


'''
def procesar_linea(linea):
    # Dividir la línea en palabras (números)
    palabras = linea.split()

    # Contar la cantidad de números y calcular la suma
    cantidad_numeros = 0
    suma_numeros = 0

    for palabra in palabras:
        try:
            numero = int(palabra)
            cantidad_numeros += 1
            suma_numeros += numero
        except ValueError:
            continue

    return cantidad_numeros, suma_numeros


try:
    while True:
        # Leer una línea de la entrada estándar
        linea = input().strip()

        # Salir del bucle si la línea está vacía
        if not linea:
            break

        # Procesar la línea y obtener resultados
        cantidad, suma = procesar_linea(linea)

        # Imprimir resultados para la línea actual
        print(cantidad, suma)

except EOFError:
    pass


