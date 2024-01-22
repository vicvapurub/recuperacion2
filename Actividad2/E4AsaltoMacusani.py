'''

| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 16/01/2024
| Ejercicio4: El asalto en Macusani

'''
def calcular_clave_caja_fuerte(n):
    clave = sum(range(1, n + 1))
    return clave

n = int(input())
        
if n >= 0:
    clave_caja_fuerte = calcular_clave_caja_fuerte(n)
    print(clave_caja_fuerte)


