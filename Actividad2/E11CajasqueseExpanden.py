'''
| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 18/01/2024
| Ejercicio11: Cajas que se expanden

'''
# entrada de datos
a, b = map(int, input().split())

# cálculo de la capacidad de las cajas
caja_normal = (b // a) + (1 if b % a != 0 else 0)
caja_mas_grande = int(caja_normal * 1.5)

# salida de resultados
if a == 1:
    print(caja_mas_grande, caja_mas_grande)
else:
    print(caja_normal, caja_mas_grande)


