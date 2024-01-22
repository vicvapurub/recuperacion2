'''
| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 18/01/2024
| Ejercicio10: Tortillas horneadas

'''
# entrada de datos
a = int(input())
b = int(input())

# aplicacion de restricciones
if 1 <= a <= 1000 and 1 <= b <= 1000:
    # Cálculo de la cantidad de maíz necesaria
    area_tortilla = (a + 5) * (b + 3)
    gramos_maiz = area_tortilla

    # salida del resultado
    print(gramos_maiz)

