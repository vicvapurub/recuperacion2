'''
Alumno: Ramírez Reyes Víctor Manuel
Fecha: 15/01/2024 
Problema: Operaciones con Strings

'''

# Capturar el texto en una línea
texto = input()

# Dividir el texto en palabras
palabras = texto.split()

# Crear una lista para almacenar el resultado
resultado = []

# Iterar a través de las palabras y aplicar la alternancia de minúsculas y mayúsculas
for i, palabra in enumerate(palabras):
    if i % 2 == 0:
        # Si la posición es par, convertir a minúsculas
        resultado.append(palabra.lower())
    else:
        # Si la posición es impar, convertir a mayúsculas
        resultado.append(palabra.upper())

# Crear una cadena uniendo los elementos de la lista con espacios
resultado = ' '.join(resultado)

# Imprimir el resultado
print(resultado)



