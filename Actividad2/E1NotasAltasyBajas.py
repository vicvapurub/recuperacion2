'''

| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 16/01/2024
| Ejercicio1: Notas Altas y Notas Bajas

'''
def calcular_promedio(calificaciones):
    return round(sum(calificaciones) / len(calificaciones), 2)
    
n = int(input())
calificaciones = list(map(int, input().split()))

# Ordenar calificaciones
calificaciones.sort()

# Calcular la posicion de la mediana
posicion_mediana = (n + 1) // 2 - 1
mediana = calificaciones[posicion_mediana]

# Dividir las calificaciones en notas bajas y altas
notas_bajas = calificaciones[:posicion_mediana]
notas_altas = calificaciones[posicion_mediana + 1:]

# Calcular los promedios
promedio_bajas = calcular_promedio(notas_bajas)
promedio_altas = calcular_promedio(notas_altas)

# Imprimir resultados
print(' '.join(map(str, calificaciones)))
print(mediana)
print(format(promedio_bajas, ".2f"))
print(format(promedio_altas, ".2f"))





