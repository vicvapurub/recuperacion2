'''

| Autor: Ramirez Reyes Vicor Manuel
| Fecha: 16/01/2024
| Ejercicio5: La parranda 2

'''
def calcular_tragos(n):
    if n % 2 == 0:
        tragos_por_persona = n // 2
        return tragos_por_persona
    else:
        return 0


n = int(input())
        
tragos = calcular_tragos(n)

print(tragos)
        
