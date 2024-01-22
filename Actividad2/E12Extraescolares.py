'''
| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 18/01/2024
| Ejercicio12: Extraescolares

'''
# Entrada de datos
horas_cumplidas = int(input())

# Verificación de limites
if 0 <= horas_cumplidas <= 480:
    # Calculo de las horas requeridas
    horas_requeridas = 60 * 8

    # Verificacion y salida de resultados
    if horas_cumplidas >= horas_requeridas:
        print("Cumplió al 100% sus créditos")
    else:
        horas_pendientes = horas_requeridas - horas_cumplidas
        print(f"Debe {horas_pendientes} horas")

